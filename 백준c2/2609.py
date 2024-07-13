import sys
import math

px = list(map(int,sys.stdin.readline().split()))
# for j in range(2,px[0]+1):
#     if px[0]%j == 0:
#         px1.append(j)
# for k in range(2,px[1]+1):
#     if px[1]%k == 0:
#         if px[1]%k in px1:
#             px.append(k)
# max_divser = max(px1)
# for i in px:
#     i//

# print(px1)

print(math.gcd(px[0],px[1]))
print(math.lcm(px[0],px[1]))
