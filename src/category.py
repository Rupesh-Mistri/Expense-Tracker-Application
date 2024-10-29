# src/category.py
import pandas as pd
import os

class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def to_dict(self):
        return {"name": self.name}
    
    
def add_category():
    name = input("Enter category name: ")
    new_category = Category(name)
    df = pd.DataFrame([new_category.to_dict()])
    file_exists = os.path.isfile('../data/category.csv')
    df.to_csv('../data/category.csv', mode='a', header=not file_exists, index=False)
    print(f"Category '{name}' added.")


def read_category():
    df=pd.read_csv('../data/category.csv')
    print(df)

def update_category():
    name = input("Enter the category name you want to update: ")
    update_name = input("Enter the new category name: ")

    if os.path.isfile('../data/category.csv'):
        df = pd.read_csv('../data/category.csv')
        if name in df['name'].values:
            df.loc[df['name'] == name, 'name'] = update_name
            df.to_csv('../data/category.csv', index=False)
            print(f"Category '{name}' updated to '{update_name}'.")
        else:
            print(f"Category '{name}' not found.")
    else:
        print("Category file does not exist.")


def delete_category():
    name = input("Enter the category name which you want to delete: ")
    df = pd.read_csv('../data/category.csv')
    
    if name in df['name'].values:
        df = df[df['name'] != name]
        
        df.to_csv('../data/category.csv', index=False)
        print(f"Category '{name}' deleted.")
    else:
        print(f"Category '{name}' not found.")

add_category()
# read_category()
# update_category()
# delete_category()