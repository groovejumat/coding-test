print("큐의 길이 N을 입력하세요")
Ne = int(input())

queue = []

for _ in range(Ne) :
    print("수행할명령어 / 숫자 입력")
    cmd = input().split()
    print(cmd)
    num = None
    if cmd[1] : 
        num = int(cmd[1])
    if cmd[0] == 'push' :
        queue.append(num)

    elif cmd[0] == 'pop' :
        queue.pop
        print(-1)


