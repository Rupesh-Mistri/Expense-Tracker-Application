from category import Category
from expense import Expense
import pandas as pd
import os
from datetime import date

class ExpenseTracker:
    def __init__(self):
        self.category_file = '../data/category.csv'
        self.expense_file = '../data/expense.csv'
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from CSV file when the application starts."""
        if os.path.isfile(self.expense_file):
            self.expenses_df = pd.read_csv(self.expense_file)
        else:
            self.expenses_df = pd.DataFrame(columns=["amount", "date", "category", "description"])

    def add_category(self):
        name = input("Enter category name: ")
        new_category = Category(name)
        df = pd.DataFrame([new_category.to_dict()])
        file_exists = os.path.isfile(self.category_file)
        df.to_csv(self.category_file, mode='a', header=not file_exists, index=False)
        print(f"Category '{name}' added.")

    def read_categories(self):
        if os.path.isfile(self.category_file):
            df = pd.read_csv(self.category_file)
            print("Categories:")
            print(df)
        else:
            print("No categories found.")

    def update_category(self):
        name = input("Enter the category name you want to update: ")
        update_name = input("Enter the new category name: ")

        if os.path.isfile(self.category_file):
            df = pd.read_csv(self.category_file)

            if name in df['name'].values:
                df.loc[df['name'] == name, 'name'] = update_name
                df.to_csv(self.category_file, index=False)
                print(f"Category '{name}' updated to '{update_name}'.")
            else:
                print(f"Category '{name}' not found.")
        else:
            print("Category file does not exist.")

    def delete_category(self):
        name = input("Enter the category name which you want to delete: ")
        
        if os.path.isfile(self.category_file):
            df = pd.read_csv(self.category_file)

            if name in df['name'].values:
                df = df[df['name'] != name]
                df.to_csv(self.category_file, index=False)
                print(f"Category '{name}' deleted.")
            else:
                print(f"Category '{name}' not found.")
        else:
            print("Category file does not exist.")

    def add_expense(self):
        self.read_categories()  # Show categories before adding expense
        amount = float(input("Enter expense amount: "))
        exp_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ") or str(date.today())
        choose_category = input("Enter name of category: ")
        description = input("Enter description: ")

        new_expense = Expense(amount, exp_date, choose_category, description)
        df = pd.DataFrame([new_expense.to_dict()])
        file_exists = os.path.isfile(self.expense_file)
        df.to_csv(self.expense_file, mode='a', header=not file_exists, index=False)
        print(f"Expense with data\n Amount: {amount}\n Date: {exp_date}\n Category: {choose_category}\n Description: {description}\n Successfully Added")

    def read_expenses(self):
        if not self.expenses_df.empty:
            print("Expenses:")
            print(self.expenses_df)
        else:
            print("No expenses found.")

    def update_expense(self):
        if not self.expenses_df.empty:
            print("Current Expenses:")
            print(self.expenses_df)

            index = int(input("Enter the index of the expense you want to update: "))

            if index < 0 or index >= len(self.expenses_df):
                print("Invalid index.")
                return

            new_amount = input("Enter new expense amount (or leave blank to keep current): ")
            new_date = input(f"Enter new date (YYYY-MM-DD) or leave blank to keep current ({self.expenses_df.loc[index, 'date']}): ")
            new_category = input(f"Enter new category or leave blank to keep current ({self.expenses_df.loc[index, 'category']}): ")
            new_description = input(f"Enter new description or leave blank to keep current ({self.expenses_df.loc[index, 'description']}): ")

            # Update DataFrame with new values
            self.expenses_df.loc[index, 'amount'] = float(new_amount) if new_amount else self.expenses_df.loc[index, 'amount']
            self.expenses_df.loc[index, 'date'] = new_date if new_date else self.expenses_df.loc[index, 'date']
            self.expenses_df.loc[index, 'category'] = new_category if new_category else self.expenses_df.loc[index, 'category']
            self.expenses_df.loc[index, 'description'] = new_description if new_description else self.expenses_df.loc[index, 'description']

            self.expenses_df.to_csv(self.expense_file, index=False)
            print("Expense updated successfully.")
        else:
            print("No expenses found.")

    def delete_expense(self):
        if not self.expenses_df.empty:
            print("Current Expenses:")
            print(self.expenses_df)

            index = int(input("Enter the row index you want to delete: "))

            if index < 0 or index >= len(self.expenses_df):
                print("Invalid index. Please enter a valid row index.")
                return

            self.expenses_df.drop(index=index, inplace=True)
            self.expenses_df.reset_index(drop=True, inplace=True)
            self.expenses_df.to_csv(self.expense_file, index=False)
            print(f"Expense at index {index} deleted successfully.")
        else:
            print("No expenses found.")

    def generate_report(self,):
        """Generate a report of total expenses for a specific period."""
        if self.expenses_df.empty:
            print("No expenses available to generate reports.")
            return
        period=input("Enter daily or weekly or monthly to generate report:")
        # Convert the 'date' column to datetime
        self.expenses_df['date'] = pd.to_datetime(self.expenses_df['date'])

        # Calculate the total expenses based on the specified period
        if period == 'daily':
            report = self.expenses_df.groupby(self.expenses_df['date'].dt.date)['amount'].sum()
        elif period == 'weekly':
            report = self.expenses_df.groupby(self.expenses_df['date'].dt.to_period('W').apply(lambda r: r.start_time))['amount'].sum()
        elif period == 'monthly':
            report = self.expenses_df.groupby(self.expenses_df['date'].dt.to_period('M').apply(lambda r: r.start_time))['amount'].sum()
        else:
            print("Invalid period. Please choose 'daily', 'weekly', or 'monthly'.")
            return

        print(f"Total expenses {period}:")
        print(report)
