import os
import json
import hashlib
import xml.etree.ElementTree as ET
from expense import expenses


tree = ET.parse('config.xml')
root = tree.getroot()

class user :
    def __init__(self ,name, pswd):
        self._name = name
        self._budget=0
        self._expense_obj = expenses()
        self._remain = 0
        self._passwd=hashlib.sha256(pswd.encode('utf-8')).hexdigest()
        
        
    def verify(self, pswd):
        return (hashlib.sha256(pswd.encode('utf-8')).hexdigest() == self._passwd)


    def update_budget(self,budget):
        self._budget += int(budget)
        self._remain += int(budget)


    def add_detail_wrapper(self, month, budg, **kwargs):
        self._budget=budg
        self._remain=budg
        self._expense_obj.add_detail(month, **kwargs)
        if self._expense_obj.total>self._budget:
            print("Expense got overbudgeted")
            add = int(input("Add budget to current month"))
            self.update_budget(add)
        self._remain -= int(self._expense_obj.total)
        # self.write_json()

    # Still figuring out how to write this object to JSON
    def write_json(self):    
        with open(root[0][4].text, 'w') as f:
            f.close()
        if os.stat(root[0][4].text).st_size == 0:
            jsonified_s = json.dumps(self.__dict__, indent=4)
            with open(root[0][4], "w") as outfile:
                outfile.write(jsonified_s)
                outfile.close()
        else:
            with open(root[0][4]) as file:
                file_data = json.load(file)
                temp=file_data
                temp.append(self.__dict__)
                with open(root[0][4], 'w') as out_file:
                    json.dump(file_data, out_file, indent = 4)


    def print_remain(self):
        print("The amount remaining is {}". format(self._remain))