# # 수 찾기
# import sys
# input = sys.stdin.readline
# n = int(input())
# number1 = set(map(int,input().split()))
# m = int(input())
# list_1 = set(map(int,input().split()))
# for i in list_1:
#     if i in number1:
#         print(1)
#     else:
#         print(0)
import sys

n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for i in M:
    if i in N:
        print(1)
    else:
        print(0)


