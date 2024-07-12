import sys
fake = []
count = int(sys.stdin.readline())
jumsu = list(map(int,sys.stdin.readline().split()))

M = max(jumsu)
for i in jumsu:
    fake.append(i/M*100)
avg = sum(fake)/count
print(avg)