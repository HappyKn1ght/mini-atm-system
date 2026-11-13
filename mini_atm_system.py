current_balance = 0
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def check_balance():
    print(f"Current Balance: ₹{current_balance:.2f}")

def deposit():
    global current_balance
    deposit_cash = float(input("Enter an amount to be deposited: "))
    if deposit_cash <= 0:
        print(f"{RED}That's not a valid amount{RESET}")
    else:
        current_balance += deposit_cash
        print(f"{GREEN}You deposited: ₹{deposit_cash:.2f}\nUpdated Balance: ₹{current_balance:.2f}{RESET}")


def withdraw():
    global current_balance
    withdraw_cash = float(input("Enter amount to be withdrawn: "))
    if withdraw_cash > current_balance:
        print(f"{RED}Insufficient balance!{RESET}")
    elif withdraw_cash <= 0:
        print("Amount must be greater than 0")
    else:
        current_balance -= withdraw_cash
        print(f"{YELLOW}You withdrew: ₹{withdraw_cash:.2f}\nAvailable Balance: ₹{current_balance:.2f}{RESET}")

def show_menu():
    print(f'''{CYAN}Choose option:
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit{RESET}''')

def print_line():
    print("-" * 40) 

def main():
    print("===== ATM SYSTEM =====")
    while True:
        show_menu()
        option = (input("Enter Your Option(1-4): "))

        if option == '1':
            print_line()
            check_balance()
            print_line()

        elif option == '2':
            print_line()
            deposit()
            print_line()

        elif option == '3':
            print_line()
            withdraw()
            print_line()

        elif option == '4':
            print_line()
            print("Thank you for using our ATM System\n\nVisit us again!")
            print_line()
            break
        
        else:
            print_line()
            print("That is not a valid choice!\n\nEnter valid input from below:-")
            print_line()
 

if __name__ == "__main__":
    main()