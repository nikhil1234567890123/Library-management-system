#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# MODULE TO CONFIRMED CONNECTION
# import mysql.connector
import sqlite3

# con = mysql.connector.connect(host="localhost", user="root", passwd="python", database="library")
con=sqlite3.Connection('library')
cur=con.cursor()
cur.execute("create table if not exists book(Name varchar(20), Code varchar(20) PRIMARY KEY, Total Books number(50), Subject varchar(20))")
cur.execute("create table if not exists issue(Name varchar(20), Reg No varchar(20) PRIMARY KEY, Book Code number(50), Date varchar(20))")
cur.execute("create table if not exists submit(Name varchar(20),Reg No varchar(20) PRIMARY KEY, Book Code number(50), Date varchar(20))")




# MODULE TO ADD BOOKS
def addbook():
    b = input("Enter BOOK Name:")
    c = input("Enter BOOK Code:")
    t = input("Total Books:")
    s = input("Enter Subject:")
    cur.execute("INSERT INTO book values(?,?,?,?)",(b,c,t,s))
    con.commit()
    print(">----------------------------------------<")
    print("Data Entered Successfully")
    print(">----------------------------------------<")
    main()


# MODULE FOR ISSUING BOOKS
def issueb():
    n = input("Enter Name:")
    r = input("Enter Reg No:")
    c = input("Enter Book Code:")
    d = input("Enter Date:")
    cur.execute("INSERT INTO issue values(?,?,?,?)",(n,r,c,d))
    print(">----------------------------------<")
    print("Book issued to:", n)
    print(">----------------------------------<")
    bookup(c, -1)


# MODULE FOR SUBMISSION OF BOOKS
def submitb():
    n = input("Enter Name:")
    r = input("Enter Reg No:")
    c = input("Enter Book Code:")
    d = input("Enter Date:")
    cur.execute("INSERT INTO submit values(?,?,?,?)",(n,r,c,d))
    con.commit()
    print(">--------------------------------------<")
    print("Book Submitted from:", n)
    print(">--------------------------------------<")
    bookup(c, 1)


def bookup(co, u):
    cur.execute("select total from book where code =(?)",(co,))
    myresult = cur.fetchone()
    # t = myresult[2] + u
    cur.execute("update book set total =total+(?) where code =(?)",(u,co))
    con.commit()
    main()


# MODULE TO DELETE BOOKS FROM RECORD
def dbook():
    ac = input("Enter Book Code:")
    cur.execute("delete from book where code=(?)",(ac,))
    con.commit()
    print(">----------------------------------<")
    print("Data Deleted Successfuly ")
    print(">----------------------------------<")
    main()


# MODULE TO DISPLAY BOOKS
def dispbook():
    a = "select * from book"
    cur.execute(a)
    myresult = cur.fetchall()
    for i in myresult:
        print("Book Name:", i[0])
        print("Book Code:", i[1])
        print("Total:", i[2])
        print(">------------------------------------<")
    main()


# MODULE TO UPDATE BOOKS
def modify():
    print('*********Menu for modification of details**********')
    print(">-----------------------------------------------------<")
    print("\n")
    print('1.Book code')
    print('2.Book Name')
    print('3.Total Books')
    ch1=input('enter your choice from the menu which you want to modify:')
    ch2=input('enter option to be changed on basis of:')
    if ch1=='1':
        if ch2=='1':
            print("\n")
            x=input('enter book code to be added:')
            z=input('enter book code to be removed:')
            y='update book set code="{}" where code="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('enter book code to be changed to:')
            z=input('enter book name whose code has to be changed:')
            y='update book set code="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('enter book code to be changed to:')
            z=int(input('enter total books whose code has to be changed:'))
            y='update book set code="{}" where total book="{}"'.format(x,z)
    elif ch1=='2':
        if ch2=='1':
            print("\n")
            x=input('enter book name to be changed to:')
            z=input('enter book code has to be changed:')
            y='update book set book Name="{}" where code="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=input('enter book name to be changed to:')
            z=input('enter book name has to be removed:')
            y='update book set name="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=input('enter book name to be changed to:')
            z=int(input('total book on basis of change is made:'))
            y='update book set name="{}" where name="{}"'.format(x,z)
    elif ch1=='3':
        if ch2=='1':
            print("\n")
            x=int(input('enter total books to be changed to:'))
            z=int(input('book code on basis of change is made:'))
            y='update book set total="{}" where code="{}"'.format(x,z)
        elif ch2=='2':
            print("\n")
            x=int(input('enter total books to be changed to:'))
            z=int(input('book name on basis of change is made:'))
            y='update book set total="{}" where name="{}"'.format(x,z)
        elif ch2=='3':
            print("\n")
            x=int(input('enter total books to be changed to:'))
            z=input('total books to be removed :')
            y='update book set total="{}" where total="{}"'.format(x,z)
    cur.execute(y)
    con.commit()
    print(">------------------------------------------<")
    print("updated record")
    print(">--------------------------------------------<")



#MODULE TO SEARCH BOOK
def search_book():
    A="select*from book"
    cur.execute(A)
    for i in cur:
        i=list(i)
    print(">--------------------------------------------------<")
    print("Menu for searching details on the basis of choice")
    print('1.Book code')
    print('2.Book Name')
    print('3.Total Books')
    print("\n")
    ch=input('enter a choice:')
    if ch=='1':
        x=input('enter the book code to be searched:')
        if i[0]==x:
            y='select*from book where code="{}"'.format(x)
            cur.execute(y)
            q=cur.fetchall()
            print(q)
        else:
            print("code not found")
    elif ch=='2':
        x=input('enter the book name to be searched:')
        if i[1]==x:
            y='select*from book where name="{}"'.format(x)
            cur.execute(y)
            q=cur.fetchall()
            print(q)
        else:
            print("name not found")          
    elif ch=='3':
        x=input('enter the total book to be searched')
        if i[2]==x:
            y='select*from book where total="{}"'.format(x)
            cur.execute(y)
            q=cur.fetchall()
            print(q)
        else:
            print("total books not found")
    main()
   


            
            
            
            

# MAIN FUNCTION
def main():
    print(">--------------------------------------------<")
    print("""       WELCOME TO OPEN LIBRARY      """)
    print(">--------------------------------------------<")
    print(">---------------------------------------------<")
    print("""       MADE BY NIKHIL KAUNDAL          """)
    print(">--------------------------------------------<")
    print(">--------------------------------------------<")
    print("""
                            LIBRARY MANAGEMENT
         1. ADD BOOK
         2. ISSUE BOOK
         3. SUBMIT BOOK
         4. DELETE BOOK
         5. DISPLAY BOOKS
         6. UPDATE BOOKS
         7. SEARCH BOOKS
         8. EXIT
         """)
    choice = input("Enter Task No:")
    print(">--------------------------------------------------<")
    if (choice == '1'):
        addbook()
    elif (choice == '2'):
        issueb()
    elif (choice == '3'):
        submitb()
    elif (choice == '4'):
        dbook()
    elif (choice == '5'):
        dispbook()
    elif (choice == '6'):
        modify()
    elif (choice == '7'):
        search_book()
    elif (choice == '8'):
        print(""" THANKS FOR VISITING OUR LIBRARY """)
    else:
        print("wrong choice,Try again")
        main()


def pswd():
    ps = input("Enter password:")
    if ps == "python":
        main()
    else:
        print("wrong password,Try again")
        pswd()


pswd()


