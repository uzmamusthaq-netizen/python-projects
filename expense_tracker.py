print("================================")
print("       EXPENSE TRACKER")
print("================================")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append([name, amount])

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print(expense[0], "=", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total Expense =", total)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")