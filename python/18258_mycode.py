print("큐의 길이 N을 입력하세요")
Ne = int(input())

queue = []
len = 0

for _ in range(Ne) :
    # print("수행할명령어 / 숫자 입력")
    cmd = input().split()
    # print(cmd)
    if cmd[0] == 'push' :
        len += 1
        queue.append(cmd[1])
        print(cmd[1])

    elif cmd[0] == 'pop' :
        if len == 0 :
            print(-1)
        else :
            len = len - 1
            print(queue.pop(0))
    elif cmd[0] == 'front' :
        if len == 0 :
            print(-1)
        else :
            print(queue[0])
    
    elif cmd[0] == 'back' :
        if len == 0 :
            print(-1)
        else :
            print(queue[len-1])
    elif cmd[0] == 'empty' :
        if len == 0:
            print(1)
        else :
            print(0)
    elif cmd[0] == 'size' :
        print(len);


