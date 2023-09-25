import os
os.system("cls")

class Animals:
    def __init__(self,turi,nomi,yoshi,fly = False):
        self.turi = turi
        self.nomi = nomi
        self.yoshi = yoshi
        self.fly = fly
    
class Otxorlar(Animals):
    def __init__(self, turi, nomi, yoshi, fly=False):
        super().__init__(turi, nomi, yoshi, fly)

    def input(self):
        self.turi = input("Hayvon turini kiriting: ")
        self.nomi = input("hayvon nomini kiriting: ")
        self.yoshi = int(input("Hayvon yoshini kiriting: "))
        self.fly = bool(input("Hayvon uchaoladimi(True or False): "))
        
    def output(self):
        print(f"{self.turi}  {self.nomi}  {self.yoshi}  {self.fly}")


    def canfly(self):
        if self.fly == True:
            print("Bu hayvon uchaolar ekan !!!")
        else:
            print("Bu hayvon uchaolmas ekan !!!")
class Yirtqichlar(Otxorlar):
    def __init__(self, turi, nomi, yoshi, fly=False):
        super().__init__(turi, nomi, yoshi, fly)

    def eating(self,typ,eatTyp):
        if typ == self.turi:
            print(f"Ushbu hayvon {eatTyp} turdagi o'somlikni sevib istemol qiladi")
        else:
            print(f"Ushbu hayvon {self.turi} hayvon sanaladi va bunday narsani yemaydi")


hy = Yirtqichlar("O'txo'r","Qoy",5,False)
hy.output()
hy.eating("O'txo'r","Beda")
hy.canfly()

        
        