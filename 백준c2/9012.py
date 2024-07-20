# 괄호
import sys
input = sys.stdin.readline
n = int(input())

# for i in range(n):
    # countL  =0
    # countR = 0
    # rhkfgh = input().strip()
    # for i in rhkfgh:
    #     if i == '(':
    #         countL += 1
    #     elif i == ')':
    #         countR += 1
    # if countL == countR:
    #     print('YES')
    # else:
    #     print('NO')
for i in range(n):
    count  =0
    rhkfgh = input().strip()
    for i in rhkfgh:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            count += 100
    if count == 0:
        print('YES')
    else:
        print('NO')