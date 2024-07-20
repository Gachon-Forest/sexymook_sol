#숫자카드 2
import sys
input = sys.stdin.readline

_ = int(input())
N = list(map(int,input().split()))
_ = int(input())
M = list(map(int,input().split()))

dict1 =  {}
for n in N:
    if n in dict1:
        dict1[n] += 1
    else:
        dict1[n] = 1

# print(dict1)
print(' '.join(str(dict1[m]) if m in dict1 else '0' for m in M))    



# for i in range(len(M)): 
#     count = N.count(M[i])  
#     output += str(count) + ' '  