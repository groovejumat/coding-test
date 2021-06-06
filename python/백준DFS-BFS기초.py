from sys import stdin
n, m, v = map(int, stdin.readline().split()) #한줄 씩 입력값을 받는다.
matrix = [[0] * (n + 1) for _ in range(n + 1)] #정점을 통해서 n*n의 배열 값을 만든다.
print(matrix);

for _ in range(m): #간선의 갯수 만큼 이동 할 수 있다.
    line = list(map(int, stdin.readline().split())) #줄 단위로 값을 쪼갠다.
    matrix[line[0]][line[1]] = 1 
    matrix[line[1]][line[0]] = 1

def bfs(start):
    visited = [start]
    queue = [start]
    print("BFS", visited)
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                print("BFS", visited)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited += [start]
    print("DFS", visited)
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

print(*dfs(v,[]))
print(*bfs(v))
print(matrix)