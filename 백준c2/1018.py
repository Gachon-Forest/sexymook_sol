    # 체스판 다시칠하기
import sys
input = sys.stdin.readline
x,y = map(int,input().split())
cheseBord = []
for i in range(y):
    a= input()
    a = a.replace('\n','')
    cheseBord.append(a)
print(cheseBord)
