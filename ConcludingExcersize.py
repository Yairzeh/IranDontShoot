import json

'''
1: I researched 3 different configuration file types- JSON, INI and YAML,
I chose the JSON configuration type because it's supported in Python by default (unlike YAML),
It's clear, organized, and easy for someone to read and manually modify,
JSON files have a strict structure that helps prevent bugs (unlike INI files, which can sometimes have undetected soft bugs),
and it's very convenient and easy to dump and save changes at the end.

2: similarly to how all the different actions are done, I made a "save & exit" action in the action menu.
 Additionally I added an "Exit out of program" command to the main menu, so you could turn off the program entirely.
'''
FILE_DIRECTORY = 'ConfigurationFile.json'


# Functions:

def main_menu():
    """
    shows the main menu and its options, asks for input on what to do and returns it.
    """
    what_to_do = input('\nWelcome! Here are your options:\n\n'
                       '[1] Log-in\n'
                       '[2] Exit out of program\n'
                       'Enter your choice: ')
    return what_to_do


def open_file():
    """
    opens the JSON configuration file and returns it.
    """
    with open(FILE_DIRECTORY, 'r') as file:
        return json.load(file)


def open_account(accounts):
    """
    asks for account number, checks if it exists in the JSON file,
    if not - raises ValueError.
    if it exists - ask for the password:
        if correct - returns the account.
        if incorrect - prints "Wrong password!" and raises ValueError.
    """
    success = False
    account_number = input('\nEnter account number: ')
    for account in accounts:
        if account_number == account['account_number']:
            account_index = accounts.index(account)
            success = True
            continue
    if not success:
        print('\nAccount does not exist!')
        raise ValueError('Account does not exist!')
    else:
        password_attempt = input('\nEnter password: ')
        if password_attempt == accounts[account_index]['password']:
            return accounts[account_index]
        print('\nWrong password!')
        raise ValueError('Wrong password!')


def save_to_config(accounts):
    """
    dumps the config file, with indent=2
    """
    with open(FILE_DIRECTORY, 'w') as file:
        json.dump(config, file, indent=2)


def view_balance(account):
    """
    returns the account balance!
    """
    return account['balance']


def withdraw(account):
    """
    asks for withdrawal amount,
    if amount > account balance - prints "Not enough balance!"
    else - removes the money from balance.
        *if the input can't be translated into a float, raises ValueError.
    """
    try:
        withdrawal_amount = float(input('\nEnter amount to withdraw: '))
        if withdrawal_amount > account['balance']:
            print('\nNot enough balance!')
        else:
            account['balance'] -= withdrawal_amount
            print('\nMoney Withdrawn Successfully!')
    except ValueError:
        print('\nInvalid Input!')


def deposit(account):
    """
    asks for deposit amount,
    adds it to balance.
        *if the input can't be translated into a float, raises ValueError.
    """
    try:
        deposit_amount = float(input('\nEnter amount to deposit: '))
        account['balance'] += deposit_amount
        print('\nMoney Withdrawn Successfully!')
    except ValueError:
        print('\nInvalid Input!')


def change_password(account):
    """
    asks for a new password,
    if new password is the sane as old password - prints "Password is the same!".
    else - changes the password.
    """
    new_password = input('Enter your new password: ')
    if new_password == account['password']:
        print('Password is the same!')
    else:
        account['password'] = new_password


def action_menu():
    """
    shows the action menu, asks for input on what to do and returns it.
    """
    choice = input('\n Choose an option:\n'
                   '1. Check Balance\n'
                   '2. Make a withdrawal\n'
                   '3. Make a deposit\n'
                   '4. Change password\n'
                   '5. Save & Exit\n'
                   'Enter your choice: ')
    return choice


# Program:

start = True
while start:
    '''
    if the choice returned from the main menu function is '2' - start = False (stops the while loop) and breaks.
    if the choice wasn't '2' and is different than '1' - print "Invalid input!" and continue.
        *if input was '1', it continues to run the code normally!
    '''
    main_choice = main_menu()
    if main_choice == '2':
        start = False
        print('Bye Bye!')
        break
    elif main_choice != '1':
        print('Invalid input!')
        continue

    '''
    opens the JSON file, and uses the open account to ask for account number and password,
    if all was correct, go on with code.
    if something was wrong - continues (re-enters the main menu)
    -
    if went on with code (user number and password were correct) - sets action_start to True 
    and begins a new while loop for the action menu.
    '''
    config = open_file()
    try:
        user_account = open_account(config)
        print('Success!')
    except ValueError:
        continue
    action_start = True

    while action_start:
        '''
        shows the action menu using the function, then for each possible returned choice uses it's corresponding function.
        if the number returned was not in the options, prints "Invalid input!" and continues (re-enters the action menu).
            * choices 1-4: continues after choice was made to return into the action menu.
            * choice 5: breaks after saving to exit the action menu and return to the main menu.
        '''
        action_choice = action_menu()

        if action_choice == '1':
            print(f'\nYour account balance is {view_balance(user_account)}')

        elif action_choice == '2':
            withdraw(user_account)
            continue

        elif action_choice == '3':
            deposit(user_account)
            continue

        elif action_choice == '4':
            change_password(user_account)
            continue

        elif action_choice == '5':
            save_to_config(config)
            break

        else:
            print('\nInvalid input!')
            continue
