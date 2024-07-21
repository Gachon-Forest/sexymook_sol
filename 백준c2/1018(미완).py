    # 체스판 다시칠하기
import sys
input = sys.stdin.readline
x,y = map(int,input().split())
cheseBord = []
result = []
for _ in range(x):
    cheseBord.append(input())
for i in range(x-7):
    for j in range(y-7):
        numx = 0
        numy = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if cheseBord[a][b] != 'W':
                        numx +=1
                    else:
                        numy +=1
                else:
                    if cheseBord[a][b] != 'B':
                        numx += 1
                    else:
                        numy += 1

    result.append(numx)
    result.append(numy)
print(min(result))














