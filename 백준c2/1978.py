import sys

a = int(sys.stdin.readline())
prime_num = list(map(int,sys.stdin.readline().split()))

count1 = 0

for num in prime_num:
    if num > 1:
        is_prime = True
        for nums in range(2,num+1):
            if num//nums == 0:
                is_prime = False
                break
        if is_prime:
            count1 += 1
print(count1)
            

