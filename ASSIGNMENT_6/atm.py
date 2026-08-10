balance = 100000

print("===== ATM =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    deposit = int(input("Enter amount to deposit: "))
    balance = balance + deposit
    print("Deposit successful!")
    print("Your new balance is:", balance)

elif choice == 3:
    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal successful!")
        print("Your new balance is:", balance)
    else:
        print("Insufficient funds!")
        print("You cannot withdraw more than your balance.")

elif choice == 4:
    print("Thank you for using our ATM!")

else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")