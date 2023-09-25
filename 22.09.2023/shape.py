import os
os.system("cls")

class Shape:
    def __init__(self,kiritish):
        self.kiritish = kiritish

class Line(Shape):
    def __init__(self, kiritish):
        super().__init__(kiritish)

    def line(self):
            print("******************************")
    

class Triangle(Shape):
    def __init__(self, kiritish):
        super().__init__(kiritish)

    def triange(self):
        n = 6
        for i in range(n):
            for j in range(i+1):
                if j == 0  or i == j or i == n - 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

class Rectangle(Shape):
    def __init__(self, kiritish):
        super().__init__(kiritish)
    
    def rectangle(self):
        n = 4
        m = 8
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

class Square(Shape):
    def __init__(self, kiritish):
        super().__init__(kiritish)

    def square(self):
        n = 8
        m = 8
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

   
kiritish = input("(Line Triange Rectangle Square) shulardan birini kiriting: ")

if kiritish == "Line":
    op = Line("")
    op.line()

if kiritish == "Triangle":
    op1 = Triangle("")
    op1.triange()

if kiritish == "Rectangle":
    op2 = Rectangle("")
    op2.rectangle()

if kiritish == "Square":
    op3 = Square("")
    op3.square()
 
