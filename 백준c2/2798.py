# 블랙잭

import sys
sum = 0

n,m = map(int,sys.stdin.readline().split())
card_number = list(map(int,sys.stdin.readline().split()))
def blackJack(deck,maxiam):
    max_gam = []
    for i in range(deck):
        for j in range(i+1,deck):
            for k in range(j+1,deck):
                sum_black = card_number[i] + card_number[j] + card_number[k]
                if sum_black <= maxiam:
                    max_gam.append(sum_black)
    return max(max_gam)

print(blackJack(n,m))

        






