import os
os.system("cls")

class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

class Drug(Date):
    def __init__(self, day, month, year,drug_name,company_name,date_create):
        super().__init__(day, month, year)
        self.drug_name = drug_name
        self.company_name = company_name
        self.date_create = date_create

    def input(self):
        self.day = int(input("Dori ishlab chiqarilgan sanani kiriting: "))
        self.month = int(input("Dori ishlab chiqarilgan oyni kiriting: "))
        self.year = int(input("Dori ishlab chiqarilgan yilni kiriting"))
        self.company_name = input("Dori ishlab chiqargan kompaniyani kiriting: ")
        self.date_create = input("Hozirgi vaqtni kiriting (12.12.2020): ")


        