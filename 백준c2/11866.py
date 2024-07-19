#요세푸스 순열
import sys 
input= sys.stdin.readline
n,m = map(int,input().split())
another = n
list1 = []
now_index = 0
output= []
iop ='<'
for i in range(1,n+1):
    list1.append(i)


while now_index < n:
    if (now_index+1)%m ==0:
        output.append(list1[now_index])
    else:
        list1.append(list1[now_index])
        n +=1
    now_index += 1



for i in range(another):
    if i != another-1:    
        iop += f"{output[i]},"
    elif i == another-1:
        iop += f"{output[i]}>"
print(iop)
