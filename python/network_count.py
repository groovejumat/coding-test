def solution(n, computers):
    answer = 0

    network = []
    
    for i in range(n) :
        # print(i)
        visited = []
        network += [dfs(i, visited, computers)]
        # print(network)
    
    # network = dfs(1, visited, computers)
    dup = list(set(map(tuple, network)))
    # print(dup)
    return len(dup)


def dfs(start, visited, computers) :
    visited += [start]
    for c in range(len(computers[start])) :
        if computers[start][c] == 1 and (c not in visited) :
            dfs(c, visited, computers)
    visited.sort()
    return visited