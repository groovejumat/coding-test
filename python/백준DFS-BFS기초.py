from sys import stdin
n, m, v = map(int, stdin.readline().split()) #한줄 씩 입력값을 받는다.
matrix = [[0] * (n + 1) for _ in range(n + 1)] #정점을 통해서 n*n의 배열 값을 만든다.
print(matrix);

#노드와 간선의 정보를 가지고 있는 인접행렬을 통해서 해당 문제를 풀어나간다
#인접행렬이 가지고 있는 정보는 단순하다 :: [i][j]가 서로 연결되어져 있다면, 해당 값은 1이다. 물론 그 반대도 마찬가지 이기 때문에 대칭적인 구조를 가진다

for _ in range(m): #간선의 갯수 만큼 이동 할 수 있다.
    line = list(map(int, stdin.readline().split())) #줄 단위로 값을 쪼갠다.
    matrix[line[0]][line[1]] = 1 
    matrix[line[1]][line[0]] = 1

def bfs(start):
    visited = [start] #방문 기록에 해당 값을 넣는다
    queue = [start] #queue에 해당 값을 넣는다
    print("BFS", visited)
    while queue: #해당 queue가 도는 동안
        n = queue.pop(0) #queue에 있는 맨 첫번째 값을 꺼내온다
        for c in range(len(matrix[start])): #해당 조건이 있는 matrix필드에서, 해당 시작점이 몇번째 줄에 있는지 확인한다
            if matrix[n][c] == 1 and (c not in visited): #해당 줄에서, 경로가 있고, visitied에는 없는 값을 넣는다
                visited.append(c) 
                print("BFS", visited)
                queue.append(c) #해당 queue의 값이 n으로 들어간다 (다음탐색이 되어지는 것)
    return visited

def dfs(start, visited):
    visited += [start] #첫 시작 값을 방문 값에 넣는다
    print("DFS", visited)
    for c in range(len(matrix[start])): #해당 start정보 값을 가지고 있는 행에서 부터, 정보탐색을 시작한다
        if matrix[start][c] == 1 and (c not in visited): #해당 행에서 값들을 도는 와중에, 자신이 아닌 다른 곳에 1이 있는 경우
            dfs(c, visited) #해당 값에 시작점에서 다음 dfs를 시작한다
    return visited

print(*dfs(v,[]))
print(*bfs(v))
print(matrix)