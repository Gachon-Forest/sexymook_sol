# 카드2
import sys 
from collections import deque
n = int(sys.stdin.readline())
# number = ''
# for i in range(1,n+1):
#     number += str(i)
cardDeck = deque([i for i in range(1,n+1)])


for i in range(1,len(cardDeck)):
    cardDeck.remove(cardDeck[0])
    cardDeck.rotate(-1)
# for i in range(len(cardDeck)-1):
#     cardDeck.pop(0)
#     a = cardDeck.pop(0)
#     cardDeck.insert(len(cardDeck),a)
# print(cardDeck[0])
print(cardDeck[0])