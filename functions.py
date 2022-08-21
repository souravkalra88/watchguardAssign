
from User import user
from matplotlib import pyplot as plt
import matplotlib.pyplot as plotter
import numpy as np
import getpass

list_users = {}

def new_user():

    print("Create User_name : ")
    name = input()
    passwd=getpass.getpass("Create new password : ")   
    tname = name
    name = user(tname , passwd)
    list_users[tname] = name

    print("User added")
   # pass

def verif(name, paswd):
    return list_users[name].verify( paswd)

def get_cred(func):
    n=input("Enter username : ")
    p=getpass.getpass("Enter password : ")
    if verif(n, p):
        func(n)
    else:
        print("Wrong password!")

def view_rem(name):
    if name in list_users:
        list_users[name].print_remain()
    else:
        print("User not found")

def add_expense(name):
    if len(list_users) == 0 or not(name in list_users):
        print("No existing users detected")
        pass
    else:
        detail = {}
        month=input("Enter month : ")
        budget = int(input("Enter Monthly Budget : "))
        while True:
            i=int(input("1: Enter expense\n0:End\n"))
            if i==0:
                list_users[name].add_detail_wrapper(month, budget, **detail)
                return
            key=input("Enter category : ")
            value=int(input("Enter expense : "))

            detail[key]=value

def show_expense(name):
    det=list_users[name]._expense_obj.get_history()
    for it in det:
        for k, v in it.items():
            print(k)
            print(f"Total expense : {v[0]}")
            for x, y in v[1].items():
                print(f"{x} : {y}")
    print()

def pie(name):
    
        dat = []
        print("Enter month name")
        month = input()
        print("pie called")
        val = []

        det=list_users[name]._expense_obj.get_history()
        exp = 0
        for it in det:
            for k, v in it.items():
                print(k)
                if k == month:
                    exp = v[0]
                    for x, y in v[1].items():
                        dat.append(x)
                        val.append(y)
                        
        figureObject, axesObject = plotter.subplots()

        axesObject.pie(val,

        labels=dat,

        autopct='%1.2f',

        startangle=90)


        axesObject.axis('equal')
        plotter.title(exp)
        plotter.show()

        plt.show()

def graph(name):
    dat = []
    val  = []
    det=list_users[name]._expense_obj.get_history()
    for it in det:
            for k, v in it.items():
                dat.append(k)
                val.append(v[0])
    fig = plt.figure(figsize = (10, 1000))
    plt.bar(dat, val, color ='blue',
        width = 0.4)

    plt.xlabel("Months")
    plt.ylabel("Expenses")
    plt.title("6 months data")
    plt.show()    
    

