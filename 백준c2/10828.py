#스택
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])
for i in range(n):
    comd = sys.stdin.readline().split()
    if comd[0] == 'push':
        queue.insert(0,int(comd[1]))
    elif comd[0] == 'pop':
        if queue:
            print(queue.popleft())
            
        else:
            print(-1)
    elif comd[0] == 'size':
        print(len(queue))
    elif comd[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif comd[0] == 'top':
        if queue:
            print(queue[0])
        else:
            print(-1)

         
