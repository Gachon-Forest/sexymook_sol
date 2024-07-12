class Changeint:
    def __init__(self, num):
        self.num = num

    def bina(self):
        num = self.num  # 원래 숫자를 저장하여 클래스 상태를 변경하지 않도록
        if num == 0:
            return '0'
        binaryNum = ""
        while num > 0:
            saveNum = num % 2
            binaryNum = str(saveNum) + binaryNum
            num //= 2
        return binaryNum

    def oct(self):
        num = self.num  # 원래 숫자를 저장하여 클래스 상태를 변경하지 않도록
        if num == 0:
            return "0"
        octNum = ""
        while num > 0:
            saveNum = num % 8
            octNum = str(saveNum) + octNum
            num //= 8
        return octNum

    def hexa(self):
        num = self.num  # 원래 숫자를 저장하여 클래스 상태를 변경하지 않도록
        strings = "0123456789ABCDEF"
        if num == 0:
            return "0"
        hexaNum = ""
        while num > 0:
            saveNum = num % 16
            hexaNum = strings[saveNum] + hexaNum
            num //= 16
        return hexaNum

    def __str__(self):
        return (f"10진수: {self.num}\n"
                f"2진수 : {self.bina()}\n"
                f"8진수 : {self.oct()}\n"
                f"16진수 : {self.hexa()}\n")

# 예시 사용
decimal_number = 39
converter = Changeint(decimal_number)
print(converter)