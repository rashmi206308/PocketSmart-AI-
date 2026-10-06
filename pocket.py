# ============================================================
# Coding for PocketSmart AI Project
# ============================================================

print("==========================================")
print("       POCKETSMART AI PROJECT")
print("==========================================")

# Get user's monthly budget
budget = float(input("Enter your monthly budget: ₹"))

expenses = []

while True:
    print("\n----------- POCKETSMART AI -----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Check Budget")
    print("4. AI Suggestion")
    print("5. Exit")
    print("--------------------------------------")

    choice = input("Enter your choice: ")

    # 1. Add Expense
    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: ₹"))

        expenses.append((name, amount))
        print("✅ Expense added successfully!")

    # 2. View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\nYour Expenses:")
            total = 0

            for name, amount in expenses:
                print(f"- {name}: ₹{amount:.2f}")
                total += amount

            print(f"Total Expenses: ₹{total:.2f}")

    # 3. Check Budget
    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        remaining = budget - total

        print("\n----------- BUDGET STATUS -----------")
        print(f"Monthly Budget : ₹{budget:.2f}")
        print(f"Total Spent   : ₹{total:.2f}")
        print(f"Remaining     : ₹{remaining:.2f}")

        if remaining > 0:
            print("✅ You are within your budget.")
        elif remaining == 0:
            print("⚠️ You have used your entire budget.")
        else:
            print("❌ You have exceeded your budget.")

    # 4. AI Suggestion
    elif choice == "4":
        total = sum(amount for name, amount in expenses)

        print("\n----------- AI SUGGESTION -----------")

        if total == 0:
            print("🤖 AI: You have not recorded any expenses.")
            print("Start adding your expenses to get suggestions.")

        elif total < budget * 0.50:
            print("🤖 AI: Your spending is under control.")
            print("💡 Suggestion: Continue saving money.")

        elif total < budget * 0.80:
            print("🤖 AI: Your spending is moderate.")
            print("💡 Suggestion: Reduce unnecessary expenses.")

        elif total <= budget:
            print("🤖 AI: You are close to your budget limit.")
            print("💡 Suggestion: Avoid unnecessary purchases.")

        else:
            print("🤖 AI: Your expenses are above your budget.")
            print("💡 Suggestion: Reduce spending and create a daily limit.")

    # 5. Exit
    elif choice == "5":
        print("\n==========================================")
        print("Thank you for using PocketSmart AI! 🤖")
        print("==========================================")
        break

    else:
        print("❌ Invalid choice. Please try again.")