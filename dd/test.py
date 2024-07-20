T=int(input())
for _ in range(T):
    result=0
    a=input()
    a=[i for i in a]
    for i in a:
        if i=='(':
            result+=1
        elif i==')':
            result-=1

        if result<0:
            result+=100
    if result==0:
        print('YES')
    else:
        print('N0')