import os 
os.system("cls")

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")

def large_number(n,m):
    if n > m:
        return n
    else:
        return m

def divided_number(n,m):
    return n // m

def just_print(n,m):
    print(n, m)

n = 3
m = 4
print("Salom")
multiplication_table(n)
large_number(n,m)
divided_number(n,m)
just_print(n,m)