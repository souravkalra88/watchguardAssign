from matplotlib import pyplot as plt
import matplotlib.pyplot as plotter
import numpy as np
import getpass
import functions as fn

import xml.etree.ElementTree as ET

def main():
    
    tree = ET.parse('config.xml')
    root = tree.getroot()

    while True:

        print("------------------Main Menu-----------------")
        print("1. " + root[0][0].text)
        print("2. " + root[0][1].text)
        print("3: " + root[0][2].text)
        print("4. " + root[0][3].text)
        print("0. Exit")
        option = int(input())

        match option:
            case 0:
                break
            case 1:
                fn.new_user()
            case 2:
                fn.get_cred(fn.add_expense)
            case 3:
                fn.get_cred(fn.view_rem)
            case 4:
                print("1.Show mothly data")
                print("2.Show last 6 months data")
                inp = int(input())
                if inp == 1:
                    fn.get_cred(fn.pie)
                if inp ==2:
                    fn.get_cred(fn.graph)    
            case 5:
                fn.get_cred(fn.show_expense) 
            case _:
                print("Select valid Option")

if __name__ == '__main__':
    main()

