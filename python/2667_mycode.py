from sys import stdin

mapArr = []
n = int(stdin.readline())

for _ in range(n) :
    m = str(input())
    print(list(m))
    mapArr.append(list(m))

for i in range(len(mapArr)) :
    print(mapArr[i])


connect = []

def bfs(start, connect) :
    start
    connect