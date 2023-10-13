import os
import mysql.connector as con
os.system("cls")

def create_database(database_name,table_name):
    Con = con.connect( user = 'root', password = 'Sherzod.1234', host = 'localhost')
    cur = Con.cursor()
    cur.execute(f"CREATE database if not exists {database_name}")
    if cur:
        print("Database created !!!")
    else:
        print("Database didn't created !!!")

    cur.execute(f"use {database_name}")

    cur.execute(f"""CREATE table if not exists {table_name}
    (id int primary key auto_increment, nomi text, narxi int, xotirasi int, screensize text)""")
     
    sql1 = f"INSERT into {table_name}(nomi, narxi, xotirasi, screensize) VALUES(%s,%s,%s,%s)"
    value1 = ("Redmi T10",2000100,32,"1060x570")

    sql2 = f"INSERT into {table_name}(nomi, narxi, xotirasi, screensize) VALUES(%s,%s,%s,%s)"
    value2 = ("Samsung A10",1500000,32,"1060x570")

    sql3 = f"INSERT into {table_name}(nomi, narxi, xotirasi, screensize) VALUES(%s,%s,%s,%s)"
    value3 = ("Redmi T10",2000100,32,"1000x470")

    sql4 = f"INSERT into {table_name}(nomi, narxi, xotirasi, screensize) VALUES(%s,%s,%s,%s)"
    value4 = ("iphone 11pro",5000100,64,"1060x570")

    sql5 = f"INSERT into {table_name}(nomi, narxi, xotirasi, screensize) VALUES(%s,%s,%s,%s)"
    value5 = ("iphone 15pro",2000100,128,"1060x570")

    cur.execute(sql1,value1)
    cur.execute(sql2,value2)
    cur.execute(sql3,value3)
    cur.execute(sql4,value4)
    cur.execute(sql5,value5)

    Con.commit()

    cur.execute(f"SELECT * from  {table_name} order by xotirasi")
    for x  in cur.fetchall():
            print(f"Phone id:           {x[0]}")
            print(f"Name:               {x[1]}")
            print(f"price:              {x[2]}")
            print(f"Phone memory:       {x[3]}")
            print(f"Screensize:         {x[4]}")
            print("\n\t*************************\n")    

create_database("Phones","phone")