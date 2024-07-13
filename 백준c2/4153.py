i = 0 
output = '' #출력될 거
while i == 0: #입력이 끝날떄까지 반복하기
    a = list(map(int,input().split()))
    if sum(a) == 0:# 입력된 변수값이 모두 0 이면 멈춤
        i +=1
    max_num = max(a)
    a.remove(max_num)
    if a[0]**2+a[1]**2 == a[2]**2:
        output += "right"
        output +='\n'
    else:
        output += "wrong"
        output +='\n'
print(output) #출력

    
