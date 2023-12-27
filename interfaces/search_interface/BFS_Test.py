from collections import deque

maxn = 10000
mp = [['' for _ in range(maxn)] for _ in range(maxn)]
vis = [[False for _ in range(maxn)] for _ in range(maxn)]

class Node:
    def __init__(self, x=0, y=0, step=0):
        self.x = x
        self.y = y
        self.step = step

dir = [
    [-1, 0],
    [0, -1],
    [0, 1],
    [1, 0]
]

Q = deque()

n, m = 0, 0

def In_map(x, y):
    return 0 <= x <= 14 and 0 <= y <= 14

def bfs():
    Q.append(Node(m, n, 0))
    vis[m][n] = True
    while Q:
        now = Q.popleft()
        print(f"Step for node ({now.x}, {now.y}): {now.step}")  # 打印step值
        x, y = now.x, now.y
        for i in range(4):
            xx, yy = x + dir[i][0], y + dir[i][1]
            if xx>4:
                continue
            if yy>4:
                continue
            if not In_map(xx, yy) or vis[xx][yy] or mp[xx][yy] == '#':
                continue
            vis[xx][yy] = True
            Q.append(Node(xx, yy, now.step + 1))

def main():
    global m, n ,k ,p
    m, n ,k,p= map(int, input().split())
    for i in range(0, 4):
        mp[i] = list(input())
    bfs()
    print("Yes" if vis[k][p] else "No")

if __name__ == "__main__":
    main()