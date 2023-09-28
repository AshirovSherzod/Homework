import os
from random import *
os.system("cls")

class Karta:
    def __init__(self,egasi,raqami,muddati,puli):
        self.owner = egasi
        self.__numbers = raqami
        self._validityperiod = muddati
        self.__cardmoney = puli
        self.password = 2123

    def __changePassword(self):
            self.valid_password = int(input("Enter the valid card password: "))
            if self.valid_password == self.password:
                self.new_password = int(input("Enter the new card password: "))
                self.password = self.new_password
                print(f"Congratulations your card password is changes: {self.password}")
            else:
                print("Sorry, this is not the valid password")
        
    def change(self):
        self.__changePassword()

    def output_info(self):
        print("Card owner: {:16s} card numbers:{:16d}     card valid period:{:4d}     card money:{:10d}".format(self.owner,self.__numbers,self._validityperiod,self.__cardmoney))


card = Karta("Sherzod",8600232345455656,4523,1000000)
card.output_info()
card1 = Karta("Allayor",1212232345456767,2309,4000000)
card1.output_info()

own = input("Enter the name of the cardholder for which card you want to change its password: ")
if own == card.owner:
    card.change()

if own == card1.owner:
     card1.change()