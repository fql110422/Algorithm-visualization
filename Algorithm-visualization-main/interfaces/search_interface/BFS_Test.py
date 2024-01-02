from collections import deque

maxn = 105
mp = [['' for _ in range(maxn)] for _ in range(maxn)]
vis = [[False for _ in range(maxn)] for _ in range(maxn)]
k, p = 0, 0
dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
Q = deque()

class Node:
    def __init__(self, x=0, y=0, step=0):
        self.x = x
        self.y = y
        self.step = step

def in_map(x, y):
    return 0 <= x < 15 and 0 <= y < 15

def dfs():
    while Q:
        now = Q.pop()
        for i in range(4):
            xx, yy = now.x, now.y
            while True:
                xx += dir[i][0]
                yy += dir[i][1]
                if not in_map(xx, yy) or vis[xx][yy] or mp[xx][yy] == '#':
                    break
                if in_map(xx, yy) and not vis[xx][yy] and mp[xx][yy] != '#':
                    vis[xx][yy] = True
                    now.step += 1
                    Q.append(Node(xx, yy, now.step))
                    print(f"Step for node ({xx}, {yy}): {now.step}")
                    if xx == k and yy == p:
                        return
    return

if __name__ == "__main__":
    m, n, k, p = map(int, input().split())
    for i in range(4):
        mp[i] = list(input().strip())
    for i in range(4):
        for j in range(4):
            vis[i][j] = False

    Q.append(Node(m, n, 0))
    vis[m][n] = True

    dfs()
    print("Yes" if vis[k][p] else "No")