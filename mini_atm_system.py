import math
import getpass

current_balance = 0
PIN = "3981"
#color code
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def check_balance():
    print(f"Current Balance: ₹{current_balance:.2f}")

def deposit():
    
    global current_balance
    deposit_cash = input("Enter an amount to be deposited: ")
    try:
        deposit_cash = float(deposit_cash)

        if not math.isfinite(deposit_cash) or deposit_cash <= 0:
            print(f"{RED}That's not a valid amount{RESET}")
        else:
            current_balance += deposit_cash
            print(f"{GREEN}You deposited: ₹{deposit_cash:.2f}\nUpdated Balance: ₹{current_balance:.2f}{RESET}")
    except ValueError:
        print(f"{RED}Invalid input! Please enter numbers only. Returning to main menu...{RESET}")

def withdraw():
    global current_balance
    withdraw_cash = input("Enter amount to be withdrawn: ")
    try:
        withdraw_cash = float(withdraw_cash)
        if withdraw_cash > current_balance:
            print(f"{RED}Insufficient balance!{RESET}")
        elif not math.isfinite(withdraw_cash) or withdraw_cash <= 0:
            print(f"{RED}Amount must be greater than 0{RESET}")
        else:
            current_balance -= withdraw_cash
            print(f"{YELLOW}You withdrew: ₹{withdraw_cash:.2f}\nAvailable Balance: ₹{current_balance:.2f}{RESET}")
    except ValueError:
        print(f"{RED}Invalid input! Please enter numbers only. Returning to main menu...{RESET}")
    
def show_menu():
    print(f'''{CYAN}Choose option:
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit{RESET}''')

def print_line():
    print("-" * 40) 

def verify_pin():
    attempt = 3

    while attempt > 0:
        user_input = getpass.getpass("Enter Your PIN: ", echo_char="*").strip()

        if user_input == PIN:
            print_line()
            print(f"{GREEN}Correct PIN!{RESET}\nWelcome to our ATM")
            print_line()
            return True
        else:
            attempt -= 1
            if attempt > 0:
                print_line()
                print(f"{RED}Incorrect PIN!\nYou have {attempt} {'attempt' if attempt == 1 else 'attempts'} left!{RESET}")
                print_line()           
            else:
                print_line()
                print(f"{RED}Incorrect PIN!\nToo many failed attempts. Your card has been locked.{RESET}")
                print_line()
                return False


def main():
    print("===== ATM SYSTEM =====")
    if not verify_pin():
        print("Exiting ATM system...")
        return
    while True:
        show_menu()
        option = input("Enter Your Option(1-4): ").strip()

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