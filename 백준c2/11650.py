#좌표 정렬하기
import sys
input = sys.stdin.readline
n = int(input())
demen = []

for i in range(n):
    x,y = map(int,input().split())
    demen.append((x,y))
demen.sort()
for i in range(n):
    print(demen[i][0],demen[i][1])
