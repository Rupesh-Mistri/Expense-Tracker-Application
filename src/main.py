from expense_tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    while True:
        print("***************************************")
        print("1. Add Category")
        print("2. View Category")
        print("3. Update Category")
        print("4. Delete Category")
        print("5. Add Expense")
        print("6. View Expense")
        print("7. Update Expense")
        print("8. Delete Expense")
        print("9. Generate Report")
        print("10. Exit")
        print("***************************************")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            tracker.add_category()
        elif choice =='2':
            tracker.read_categories()
        elif choice =='2':  
            tracker.update_category()
        elif choice =='3':
            tracker.update_category() 
        elif choice =='4': 
            tracker.delete_category()   
        elif choice =='5':
            tracker.add_expense()
        elif choice =='6':
            tracker.read_expenses()
        elif choice =='7':
            tracker.update_expense()
        elif choice =='8':
            tracker.delete_expense()
        elif choice == '9':
            tracker.generate_report()   
        else:
            print("> Exited")
            break
        
if __name__ == "__main__":
    main()