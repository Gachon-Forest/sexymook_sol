class PhoneBook:
    def __init__(self):
        self.contracts = []
        self.index = 0
    def __str__(self):
        return str(self.contracts[self.index])
    def add(self,name,mobile,email):
        dictPhone = {"name" : name , "mobile" : mobile, " email" : email}
        self.contracts.append(dictPhone)
    def movePreviousIndex(self):
        if self.index > 0:
            self.index -= 1

    def moveNextIndex(self):
        if self.index < len(self.contracts) - 1:
            self.index += 1


    def showPhoneBool(self):
        for i in range(len(self.contracts)):
            print(self.contracts[i])
    def showLast(self):
        print(self.contracts[-1])
    def showFirst(self):
        print(self.contracts[0])
    def deletePhone(self,idx):
        if 0 <= idx < len(self.contracts):
            self.contracts.pop(idx)
tele = PhoneBook()
tele.add("lee",'010','jungmooklee')
tele.add("kim",'011','jungloelee')
tele.showFirst()
tele.showLast()

tele.showPhoneBool()
tele.deletePhone(0)
print(tele)
tele.movePreviousIndex()
tele.moveNextIndex()
print(tele)
tele.moveNextIndex()
print(tele)