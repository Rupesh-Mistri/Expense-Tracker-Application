#expense.py
import pandas as pd
import os
from datetime import date

class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def to_dict(self):
        return {"amount": self.amount , 'date':self.date, 'category':self.category,'description':self.description}

def add_expense():
    df=pd.read_csv('../data/category.csv')
    print(df)
    
    amount =int(input("Enter expanse amount:"))
    exp_date= date.today()
    choose_category=input("Enter name of category:")
    description= input("Enter description:")
    
    new_expense= Expense(amount,exp_date,choose_category,description,)
    df = pd.DataFrame([new_expense.to_dict()])
    file_exists = os.path.isfile('../data/expense.csv')
    df.to_csv('../data/expense.csv', mode='a', header=not file_exists, index=False)
    print(f"Expense with data \n Amount:{amount} \n Date:{exp_date} \n Category: {choose_category} \n Description: {description} \n Successfully Added")

def read_expense():
    df=pd.read_csv('../data/expense.csv')
    print(df)

def update_expense():
    df = pd.read_csv('../data/expense.csv')
    print("Current Expenses:")
    print(df)

    index = int(input("Enter the index of the expense you want to update: "))
    
    if index >= len(df):
        print("Invalid index.")
        return

    new_amount = int(input("Enter new expense amount (or leave blank to keep current): ") or df.loc[index, 'amount'])
    new_date = input(f"Enter new date (YYYY-MM-DD) or leave blank to keep current ({df.loc[index, 'date']}): ")
    new_category = input(f"Enter new category or leave blank to keep current ({df.loc[index, 'category']}): ")
    new_description = input(f"Enter new description or leave blank to keep current ({df.loc[index, 'description']}): ")

    df.loc[index, 'amount'] = new_amount
    df.loc[index, 'date'] = new_date if new_date else df.loc[index, 'date']
    df.loc[index, 'category'] = new_category if new_category else df.loc[index, 'category']
    df.loc[index, 'description'] = new_description if new_description else df.loc[index, 'description']

    df.to_csv('../data/expense.csv', index=False)
    print("Expense updated successfully.")

def delete_expense():
    df = pd.read_csv('../data/expense.csv')
    print("Current Expenses:")
    print(df)
    index = int(input("Enter the row index you want to delete: "))

    if index < 0 or index >= len(df):
        print("Invalid index. Please enter a valid row index.")
        return
    df.drop(index=index, inplace=True)

    df.reset_index(drop=True, inplace=True)
    df.to_csv('../data/expense.csv', index=False)
    print(f"Expense at index {index} deleted successfully.")


# # add_expense()
# read_expense()
# update_expense()