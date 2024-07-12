num_Star = int(input("Enter the number of rows: "))
output = ""

for i in range(num_Star):
    # 각 줄의 앞에 공백을 추가합니다.
    for j in range(num_Star - i - 1):
        output += " "
    # 각 줄에 별을 추가합니다.
    for k in range(i + 1):
        output += '*'
    # 줄바꿈 추가
    output += '\n'

print(output)
