https://programmers.co.kr/learn/courses/30/lessons/42748

## my solution
```python
def solution(array, commands):
    answer = []
    for index in range(len(commands)) : 
        #print(index)
        i = commands[index][0]-1
        j = commands[index][1]
        k = commands[index][2]-1
        print(i, j, k)
        if i==j : 
            # print("잘린 배열 값 : ",array[i])
            answer.append(array[i])
        else :
            arrayt=array[i:j]
            arrayt.sort()
            # print(arrayt)
            # print("k", k)
            print("잘린 배열 값 : ",arrayt[k])
            answer.append(arrayt[k])
        
    return answer
```

## most like solution
```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```