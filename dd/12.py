class Changeint:
    def __init__(self,num):
        self.num = num
    def bina(self):
        num = self.num
        if num ==0:
            return '0'
        binaryNum = ""
        while num > 0:
            saveNum = num%2
            binaryNum = str(saveNum) + binaryNum
            num//=2
        return  binaryNum
    def oct(self):
        num = self.num
        if num == 0:
            return "0"
        octNum = ""
        while num > 0:
            saveNum = num%8
            octNum = str(saveNum) + octNum
            num//=8
        return octNum
    def deci(self):
        num = self.num
        strings = "0123456789ABCDEF"
        if num == 0:
            return "0"
        deciNum = ""
        while num > 0:
            saveNum = self.num%16
            deciNum = strings[saveNum] + deciNum
            num//=16
        return deciNum 
    def __str__(self):
        return f"2진수 : {self.bina()} 8진수 : {self.oct()} 16진수 : {self.deci()}"
sip = int(input())
jinsu = Changeint(sip)
print(jinsu.bina())
print(jinsu.oct())
print(jinsu.deci())
print(jinsu)
