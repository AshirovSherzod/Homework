class Kitob():
    def __init__(self,nomi,muallifi,narxi,nashryoti):
        self.nomi = nomi
        self.muallifi = muallifi
        self.narxi = narxi 
        self.nashiryoti = nashryoti

    def kiritish(self):
        self.narxi = input("Kitob nomini kirtiting: ")
        self.muallifi = input("Kitob mallifini kiriting: ")
        self.narxi = input("Kitob narxini kiriting: ")
        self.nashiryoti = input("Kitob nashryotini kiriting:")

    def chiqarish(self):
        print(f"Kitob nomi: {self.nomi}")
        print(f"Kitob muallifi: {self.muallifi}")
        print(f"Kitob narxi: {self.narxi}")
        print(f"Kitob nashryoti: {self.nashiryoti}")
        

kitoblar = []

for _ in range(5):
    kitob = Kitob("","","","")
    kitob.kiritish()
    kitoblar.append(kitob)

for kitob in kitoblar:
    if kitob.nashiryoti[0].upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        kitob.chiqarish()