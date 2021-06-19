from sys import stdin

mapArr = []
n = int(stdin.readline())

for _ in range(n) :
    m = str(input())
    # print(list(int(m)))
    mapArr.append(list(map(int, list(m))))

for i in range(len(mapArr)) :
    print(mapArr[i])

start = []
connect = []
dx = [0, 0, -1, 1]
dy = [1,-1,  0, 0]

def bfs(matrix, cnt, x, y):
    queue = []
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.pop()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if matrix[nx][ny] == 1:
                    cnt += 1
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt

def dfs(matrix, cnt, x, y) :
    matrix[x][y]=0

    for k in range(4) :
        nx, ny = x + dx[k], y + dy[k]
        # print(nx ,ny)
        if 0 <= nx and nx< n and 0<= ny and ny <n:
            if matrix[nx][ny] == 1 :
                cnt = dfs(matrix, cnt+1, nx, ny)
    return cnt


cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if mapArr[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(dfs(mapArr, cnt+1, i, j))

for i in range(len(mapArr)) :
    print(mapArr[i])

print(len(ans))
for i in sorted(ans):
    print(i)            