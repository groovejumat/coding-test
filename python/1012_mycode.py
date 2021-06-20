from sys import stdin

testCaseCount = int(stdin.readline())

answer = []

matrix = []

dx = [0, 0, -1, 1]
dy = [1,-1,  0, 0]


def bfs(nx, ny, m, n, matrix) :
    queue = []
    queue.append([nx, ny])
    print("넣은 큐값", queue[0])
    while len(queue) > 0 :
        x, y = queue.pop()
        for i in range(len(dx)) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < m and 0 <= ny and ny < n :
                if matrix[nx][ny] == 1 :
                    print("조건에 만족함")
                    matrix[x][y] = 0
                    queue.append([nx, ny])
             


for i in range(testCaseCount) : 
    m, n, k =  map(int, stdin.readline().split())
    matrix = [[0] * m for _ in range(n)]
    for i in range(k) :
        x, y = map(int, stdin.readline().split())
        matrix[y][x] = 1
    print(matrix)
    
    cnt = 0
    for i in range(len(matrix)) :
        for u in range(len(matrix[0])) :
            if matrix[i][u] == 1 :
                bfs(i, u, m, n, matrix)
                cnt += 1
    # print(matrix)
    answer.append(cnt)
    print("정닶값은?" , answer[0])
