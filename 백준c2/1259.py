#팰린드롬수
from sys import *

while True:
    list_fel = []
    fel = stdin.readline()
    for i in range(len(fel)-1):
        list_fel.append(fel[i])
    
    if int(fel) == 0:
        break
    elif list_fel == list(reversed(list_fel)):
        print('yes')
    else:
        print('no')

