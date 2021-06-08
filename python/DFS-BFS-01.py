from sys import stdin

n, m, v = map(int, stdin.readline().split()) #한줄 씩 입력값을 받는다.

#matrix = [[0] * (n + 1) for _ in range(n + 1)]

matrix = [[0] * (n + 1) for i in range(n + 1)] #각 한 리스트마다 [0]*(n + 1)을 채워 넣는 것을 말한다

#메트릭스에서 유저가 가지고 있는 정보를 얻는다 넣어준다

#이어진 간선에 대한 정보를 매트릭스에 반영한다
for _ in range(m) :
    start, end = map(int, stdin.readline().split())
    matrix[start][end] = 1;
    matrix[end][start] = 1;


#반영되어진 매트릭스 정보를 가시적으로 조회
for i in range(m) :
    print(matrix[i])


#BFS는 이어진 부분을 우선으로 순회하고, 그 다음으로 깊은 부분을 순회한다
def BFS(start) :
    visited = [start]
    queue = [start]
    while queue :
        q = queue.pop(0); #시작 포인트
        for c in range(len(matrix[start])):
            if matrix[q][c] == 1 and (c not in visited) : 
                visited.append(c)
                queue.append(c)
    return visited


def DFS(start, visited) :
    visited += [start]
    for q in range(len(matrix[start])):
        if matrix[start][q] == 1 and (q not in visited) :
            DFS(q, visited)
    return visited

test = BFS(v)
print(test)

visited = []
test2 = DFS(v, visited)
print(test2)