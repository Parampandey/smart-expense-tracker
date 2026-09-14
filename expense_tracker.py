import csv
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD): " )
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file :
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"Total spending in {month}: {total}\n")


def category_analysis():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("Category-wise Spending:")
    for cat, amt in categories.items():
        print(cat, ":", amt)


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Analysis")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
