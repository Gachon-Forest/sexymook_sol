#수 정렬하기
import sys
input = sys.stdin.readline
number = []
n = int(sys.stdin.readline())
for i in range(n):
    number.append(int(input()))
gg = sorted(number)
for i in gg:
    print(i)

