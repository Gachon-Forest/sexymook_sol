#이항계수 1
import sys

N,K = map(int,sys.stdin.readline().split())


for i in range(K,-1):
    N *= N-1
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*fac(n-1)
print(int(fac(N)/(fac(K)*fac(N-K))))