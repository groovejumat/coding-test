def solution(prices):
    answer = []
    for index,value in enumerate(prices) :
        #print(index, value)
        start = index + 1
        
        lowercase = 0
        for check in prices[start:]:
            #print("비교해야 하는 값 : ",value , "그리고 " ,check)
            if value <= check :
                #print("체크하는 값이 조건에 만족하므로 1초 증가")
                lowercase += 1
            #값이 떨어진 순간 루프문을 빠져나온다
            else :
                lowercase += 1
                break
        #print("lowercase : " , lowercase)
        answer.append(lowercase)
        
                
#         for index, item in enumerate(I[START:], START):
#             print(item, index)
        
        

    return answer