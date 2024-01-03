def expenses_tracker():
    expenses = {
        'Monday': 0,
        'Tuesday': 20,
        'Wednesday': 0,
        'Thursday': 0,
        'Friday': 0,
        'Saturday': 0,
        'Sunday': 0
    }
    while True:
        print("1.Add new entry ")
        print("2.remove entry ")
        print("3.view expenses ")
        print("4.calculate total spending ")
        print("5.calculate remaining budget ")
        print("Exit ")
        choice = input("enter your choice ")

        if choice == '1':
            day = input("enter the day ")
            amount = float(input("enter the spending "))
            expenses[day] += amount
            print(f"expenses of {amount} added for {day} ")

        elif choice == '2':
            day = input("Enter the day")
            if day in expenses:
                amount_removed = expenses.pop(day)
                print(f"expenses of {amount_removed} is removed for {day} ")

            else:
                print("no entry found for a specified day ")

        elif choice == '3':
            for day , amount in expenses.items():
                print(f"{day} : {amount} ")

        elif choice == '4':
            total_spending = sum(expenses.values())
            print(f"Total spending for a week : {total_spending}")

        elif choice == '5':
            budget = int(input("enter your budget "))
            remaining_budget = budget - sum(expenses.values())
            print(f"Remaining budget : {remaining_budget}")

        elif choice == '6':
            print("exit")
            break

        else:
            print("Invalid input ")

expenses_tracker()