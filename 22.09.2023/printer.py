import os
os.system("cls")

class Printer:
    def __init__(self):
        self.lists = []  

    def input_info(self,model,tezlik,tur,narx = int,yil = int):
        self.model = model
        self.tezligi = tezlik
        self.narxi = narx
        self.turi = tur
        self.yil = yil
        self.lists.append((self.model , self.tezligi , self.narxi , self.turi , self.yil))

    def output_info(self):
        for x in self.lists:
            print("{:20s} {:20s} {:20d} {:20s} {:20d}".format(x[0],x[1],x[2],x[3],x[4]))

    def sorting(self):
        res = sorted(self.lists,key = lambda x: x[2])
        for x in res:
           print("{:20s} {:20s} {:20d} {:20s} {:20d}".format(x[0],x[1],x[2],x[3],x[4]))

    def typeyear(self,yili,turi):
        for x in self.lists:
            if turi in self.lists[3] or yili in self.lists[]:
                print("{:20s} {:20s} {:20d} {:20s} {:20d}".format(x[0],x[1],x[2],x[3],x[4]))

Pr = Printer()               
while 1:
    toxtat = int(input("Printer qoshish uchun 1 ni bosing: "))
    if toxtat != 1:
        break
    md = input("Printer modelini kiriting: ")
    tz = input("printer ishlash tezligini kiriting: ")
    tr = input("Printer turini kiriting: ")
    nr = int(input("Printer narxini kiriting: "))
    yl = int(input("Printer yilinin kiriting: "))
    Pr.input_info(md,tz,tr,nr,yl)

yr = int(input("Yilni kiriting: "))
trx = input("Turini kiriting: ")

Pr.sorting()
Pr.typeyear(yr,trx)