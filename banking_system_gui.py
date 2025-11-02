import os #checks if the accounts.txt existe 
import tkinter as tk #Python library tsna3 graphical user interfaces (GUIs)(Tkinter provides various components like windows, labels, buttons, text entry fields, etc..)/By using tk as the alias,nejmou nreferiw l thinker beha mn8ir mn3awdou nektbou thinker every time
from tkinter import messagebox#This imports the messagebox module, which is a part of tkinter. The messagebox module is used to create pop-up message boxes in the application. These pop-ups are useful for displaying alerts, errors, warnings, or other messages to the user.

# File name win el account data mawjouda fi 7aletna e7na esmha accounts.txt
FILE_NAME = 'accounts.txt'

#lodes th accounts data eli msejla fi accounts.txt
def load_accounts():
    accounts = {}#list of accounts
    if os.path.exists(FILE_NAME):  # Check if the file exists
        with open(FILE_NAME, 'r') as file:#if the file does exist y7elou b read mode ('r')
            for line in file:
                # Read account data (account_number:name:balance)
                account_number, name, balance = line.strip().split(':')#ta9ra kol star and splits data by (:)
                accounts[account_number] = {'name': name, 'balance': float(balance)}#stores account's number, name and balance fi liste esmha accounts wel balance 7awlneh float w fi le5er el function treturni liste of accounts
    return accounts

def save_accounts(accounts):#save data mte3 accounts fi accounts.txt
    with open(FILE_NAME, 'w') as file:#t7el el file b write mode ('w') wich overwrite any exesting content
        for account_number, data in accounts.items():
            file.write(f"{account_number}:{data['name']}:{data['balance']}\n")#loop all over the list wtkteb lkol account number , name and balance after that the function closes the file 

# Function to create a new account
def create_account(accounts, account_number, name):
    if account_number in accounts:  # Ensure account number is unique and #ken el account number mawjoud deja t9olek rahou already exist fi liste 
        messagebox.showerror("Error", "Account number already exists!")  # Show in massege box error if the e number mawjoud
        return
    balance = 0.0  # Initial balance is set to 0
    accounts[account_number] = {'name': name, 'balance': balance}
    save_accounts(accounts)  # Save the new account to file
    messagebox.showinfo("Success", f"Account created for {name} with account number {account_number}.")#if the account dosen't exist already it will creat an account wb3d yaffichilek eli account was successfuly created 

# Function to deposit money into an account
def deposit(accounts, account_number, amount):
    if account_number not in accounts:  # tteked if the account exists
        messagebox.showerror("Error", "Account number does not exist!")  # Show error if account doesn't exist
        return
    amount = float(amount)  # Convert the amount to float
    accounts[account_number]['balance'] += amount  # tzid  the deposit amount to the balance
    save_accounts(accounts)  # Save updated account to file
    messagebox.showinfo("Success", f"Deposited ${amount}. New balance: ${accounts[account_number]['balance']}")#print el montant mte3 deposit w el changement mte3 el balance 

#function withdraws money from an account.
def withdraw(accounts, account_number, amount):
    if account_number not in accounts:  # Check if the account exists
        messagebox.showerror("Error", "Account number does not exist!")  #if the account number exist tkemel el be9i sinon t9olek mouch mawjoud wtoufa el function 8adi
        return
    amount = float(amount)  # Convert the amount to float
    if amount > accounts[account_number]['balance']:  # thebet if the withdrawal amount is greater than the available balance
        messagebox.showerror("Error", f"Insufficient funds! Current balance: ${accounts[account_number]['balance']}")#ken el montant eli bch t5rajha akther mel balnce t9olek eli folousek mtkefich
        return
    accounts[account_number]['balance'] -= amount  # Subtract the withdrawal amount from the balance
    save_accounts(accounts)  # tsejel el changement eli sarou
    messagebox.showinfo("Success", f"Withdrew ${amount}. New balance: ${accounts[account_number]['balance']}")#ken kol chy mrigel t9olek succes wtna9es lfous wtwarik rl new balance

# Function to check the balance of an account
def balance_inquiry(accounts, account_number):
    if account_number not in accounts:  # Check if the account exists
        messagebox.showerror("Error", "Account number does not exist!")  # Show error if account doesn't exist
        return
    balance = accounts[account_number]['balance']  # Get the account balance
    messagebox.showinfo("Balance", f"Account balance: ${balance}")#taffichi el balance 7aseb el account number 

# Function to remove an account
def remove_account(accounts, account_number):
    if account_number not in accounts:  # Check if the account exists
        messagebox.showerror("Error", "Account number does not exist!")  # Show error if account doesn't exist
        return
    del accounts[account_number]  # Delete the account from the dictionary
    save_accounts(accounts)  # Save the updated list of accounts to file
    messagebox.showinfo("Success", f"Account {account_number} has been removed.")

#function showes existing account eli mawjoudin fi accounts.txt
def show_existing_accounts(accounts):
    if not accounts:  # Check if there are no accounts
        messagebox.showinfo("No Accounts", "No accounts found.")# ytla3lek ki yebda mfemch accounts el msg mte3 no accounts found
        return
    account_details = "\n--- Existing Accounts ---\n"
    for account_number, data in accounts.items():
        account_details += f"Account Number: {account_number}, Name: {data['name']}, Balance: ${data['balance']}\n"
    messagebox.showinfo("Existing Accounts", account_details)#If accounts exist, it prints each account's number, name, and balance.


# Tkinter GUI Setup
def main_gui():
    accounts = load_accounts()  # Load the accounts from the file befor starting

    root = tk.Tk()  # Initialize the Tkinter window
    root.title("Simple Banking System")  # Set the window title
    root.geometry("1000x500")  # Set el taille mte3 el window to 500x500 pixels/geometry() defines the window's size.
    root.config(bg="#f5f5f5")  # Set the background color of the window

    # Title labelmel fou9 fil window
    title = tk.Label(root, text="Welcome to Simple Banking System", font=("Arial", 16, 'bold'), bg="#f5f5f5", fg="#4CAF50")
    title.pack(pady=20)#el docoration for the title

    # Function to handle account creation when the "Create Account" button is clicked
    def on_create_account():
        account_number = entry_account_number.get()  # te5ou the account number from the input 
        name = entry_name.get()  # te5ou the name from the input 
        if account_number and name:
            create_account(accounts, account_number, name)  # Call create_account() with input data
        else:
            messagebox.showerror("Error", "Please provide both account number and name.")#ken m7atitch account number we name wala wa7da fihom ytla3lek error

    # Function to handle deposit when the "Deposit" button is clicked
    def on_deposit():
        account_number = entry_account_number.get()  # Get account number from input /  n3mou Entry widget fi thinker  t3ti space ll user yekteb fih w nst3mlou el get() to acces this data
        amount = entry_amount.get()  # Get deposit amount from input 
        if account_number and amount:
            deposit(accounts, account_number, amount)  # Call deposit() with input data
        else:
            messagebox.showerror("Error", "Please provide both account number and amount.")#ken m7atitch account number we name wala wa7da fihom ytla3lek error

    # Function to handle withdrawal when the "Withdraw" button is clicked
    def on_withdraw():
        account_number = entry_account_number.get()  # Get account number from input 
        amount = entry_amount.get()  # Get withdrawal amount from input 
        if account_number and amount:
            withdraw(accounts, account_number, amount)  # Call withdraw() with input data
        else:
            messagebox.showerror("Error", "Please provide both account number and amount.")#ken m7atitch account number we name wala wa7da fihom ytla3lek error

    # Function to check balance when the "Balance Inquiry" button is clicked
    def on_balance_inquiry():
        account_number = entry_account_number.get()  # Get account number from input field
        if account_number:
            balance_inquiry(accounts, account_number)  # Call balance_inquiry() with account number
        else:
            messagebox.showerror("Error", "Please provide an account number.")#ken m7atitch account number ytla3lek error

    # Function to remove an account when the "Remove Account" button is clicked
    def on_remove_account():
        account_number = entry_account_number.get()  # Get account number from input field
        if account_number:
            remove_account(accounts, account_number)  # Call remove_account() with account number
        else:
            messagebox.showerror("Error", "Please provide an account number.")#ken m7atitch account number ytla3lek error

    # Function to show existing accounts when the "Show Existing Accounts" button is clicked
    def on_show_existing_accounts():
        show_existing_accounts(accounts)  # Call show_existing_accounts()

    # Frame to hold the input fields and labels
    frame = tk.Frame(root, bg="#f5f5f5")#root hiya l-window principal (l'interface mt3 l'application).root houa fi wostou  kolchi l'widgets ( buttons, labels, entries, ...).
    frame.pack(pady=20)#frame fi dakhil root, o yjma3 l'inputs (l'labels o l'buttons).

    # Account number input field
    tk.Label(frame, text="Account Number:", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5)#grid() arranges the widgets in a grid (rows and columns).
    entry_account_number = tk.Entry(frame, font=("Arial", 12))  # Entry field for account number
    entry_account_number.grid(row=0, column=1, padx=10, pady=5)

    # Name input field
    tk.Label(frame, text="Name:", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(frame, font=("Arial", 12))  # Entry field for name
    entry_name.grid(row=1, column=1, padx=10, pady=5)#The entry_account_number will appear in the first row and second column of the grid.There will be 10 pixels of padding on the left and right, and 5 pixels of padding above and below the widget.

    # Amount input field (for deposit and withdrawal)
    tk.Label(frame, text="Amount:", bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5)
    entry_amount = tk.Entry(frame, font=("Arial", 12))  # Entry field for amount
    entry_amount.grid(row=2, column=1, padx=10, pady=5)#The entry_amount will appear in the second row and second column of the grid.There will be 10 pixels of padding on the left and right, and 5 pixels of padding above and below the widget.

    # Buttons for actions
    button_create = tk.Button(root, text="Create Account", font=("Arial", 12), bg="#4CAF50", fg="white", command=on_create_account)# comand torbet the button click to the on_create_account() function, which handles the account creation.
    button_create.pack(fill='x', pady=10)

    button_deposit = tk.Button(root, text="Deposit", font=("Arial", 12), bg="#2196F3", fg="white", command=on_deposit)# comand torbet the button click to the on_deposit() function, which handles the account deposit.
    button_deposit.pack(fill='x', pady=10)

    button_withdraw = tk.Button(root, text="Withdraw", font=("Arial", 12), bg="#FF5722", fg="white", command=on_withdraw)# comand torbet the button click to the on_withdraw() function, which handles the account withdrawt.
    button_withdraw.pack(fill='x', pady=10)

    button_balance_inquiry = tk.Button(root, text="Balance Inquiry", font=("Arial", 12), bg="#FFC107", fg="white", command=on_balance_inquiry)# comand torbet the button click to the on_balance_inquiry() function, which handles the account balance.
    button_balance_inquiry.pack(fill='x', pady=10)

    button_remove_account = tk.Button(root, text="Remove Account", font=("Arial", 12), bg="#E91E63", fg="white", command=on_remove_account)# comand torbet the button click to the on_remove_accoun() function, which handles the account removel.
    button_remove_account.pack(fill='x', pady=10)

    button_show_existing = tk.Button(root, text="Show Existing Accounts", font=("Arial", 12), bg="#9C27B0", fg="white", command=on_show_existing_accounts)# comand torbet the button click to the on_show_existing_accounts() function, which handles the account mawjoudin fi accounts.txt.
    button_show_existing.pack(fill='x', pady=5)

    # Start the Tkinter main loop
    root.mainloop() #runs the main loop 

# Start the GUI
main_gui()#Python, Tkinter tsupporti l'creation mte3 GUI, w t5alik t3ml windows, labels, buttons, etc.
