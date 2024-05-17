import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create expenses table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS expenses 
             (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL)''')
conn.commit()

def add_expense(date, category, amount):
    c.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", (date, category, amount))
    conn.commit()

def view_expenses():
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    for expense in expenses:
        print(expense)

def view_spending_by_category():
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    categories = c.fetchall()
    for category in categories:
        print(category)

def main_menu():
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Spending by Category")
    print("4. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            date = datetime.now().strftime("%Y-%m-%d")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, amount)
            print("Expense added successfully.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_spending_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
