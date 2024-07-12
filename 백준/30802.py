import sys

kill = 0
a = int(sys.stdin.readline())
how = list(map(int,sys.stdin.readline().split()))
pen = list(map(int,sys.stdin.readline().split()))
for i in how:
    kill += (i + pen[0]-1)//pen[0]
print(kill)


max_count = a//pen[1]
print(max_count,a-max_count*pen[1])

    
    