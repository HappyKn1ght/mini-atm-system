# 🏧 Mini ATM System (Python CLI)

A clean, beginner-friendly command-line ATM simulator built in Python. This project was created from scratch to practice modular functions, loops, conditional logic, variable scope, and user input validation.

---

## ✨ Features
- **Check Balance:** Displays the current account balance formatted to two decimal places (`₹0.00`).
- **Deposit Money:** Validates positive amounts and updates the account balance in real time.
- **Withdraw Money:** Prevents overdrafts (`Insufficient balance!`) and blocks zero or negative withdrawal amounts.
- **Crash-Proof Menu:** Handles invalid menu choices cleanly without breaking the program loop.
- **Color-Coded CLI UI:** Uses ANSI escape colors and receipt-style borders for clear terminal readability.

---

## 🛠️ Tech Stack
- **Language:** Python 3 (Standard Library only — zero external dependencies)

---

## 🚀 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project folder:**
   ```bash
   cd mini-atm-system
   ```
3. **Run the program:**
   ```bash
   python main.py
   ```

---

## 💻 Sample Output
```text
===== ATM SYSTEM =====
Choose option:
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit
Enter Your Option(1-4): 2
----------------------------------------
Enter an amount to be deposited: 1000
You deposited: ₹1000.00
Updated Balance: ₹1000.00
----------------------------------------
```

---

## 🗺️ Roadmap (Future Upgrades)
- [ ] Add `try / except` and `math.isfinite()` handling for non-numeric inputs
- [ ] 4-digit PIN authentication system
- [ ] Transaction history log
- [ ] Daily withdrawal limit check
- [ ] Multi-user account support
