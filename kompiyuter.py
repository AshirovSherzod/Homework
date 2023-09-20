import os
class Computer:
    def __init__(self,nomi,rami,narxi,pros):
        self.nomi = nomi 
        self.rami = rami
        self.narxi = narxi 
        self.pros = pros

    def kiritish(self):
        self.nomi = input("Kompiyuter nomini kiriting: ")
        self.rami = int(input("Kompiyuter RAMini kiriting: "))
        self.narxi = int(input("Kompiyuter narxini kiriting: "))
        self.pros = input("KOmpiyuter protsessorini kiriting: ")

    def chiqarish(self):
        print(f"Kompiyuter nomi: {self.nomi}")
        print(f"Kompiyuter RAMi: {self.rami}")
        print(f"Kompiyuter narxi: {self.narxi}")
        print(f"Kompiyuter protsessori: {self.pros}")

cam = []
for _ in range(5):
    comp = Computer("",0,0,"")
    comp.kiritish()
    cam.append(comp)

for comp in cam:
    if comp.rami > 4 and comp.rami < 16:
        comp.chiqarish()