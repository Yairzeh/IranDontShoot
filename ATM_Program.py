# Importing relevant functions from utils.py
from utils import load_json_file
from utils import dump_to_json

# Setting the config.json file path
CONFIG_FILE_PATH = 'config.json'


# Creating an Account class and methods:
class Account:
    """
    Class for a bank account that contains: account number, password, balance
    that can perform the following methods:
    - printing balance, withdrawal, deposit, changing the password, saving to config,
    and loading the account from the config file.
    """

    def __init__(self, account_number, password, balance):
        self.account_number = account_number
        self.__password = password
        self.__balance = balance

    def print_balance(self):
        """
        prints the account balance.
        """
        print(f'\nYour balance is: {self.__balance}')

    def withdraw(self):
        """
        withdraws the account from account, unless:
        - withdrawal amount is negative, greater than balance or not a number, then raises a ValueError correspondingly.
        """
        try:
            withdrawal_amount = float(input('\nEnter Withdrawal amount: '))
            if withdrawal_amount > self.__balance:
                raise ValueError('Not enough balance!')
            if withdrawal_amount < 0:
                raise ValueError('Withdrawal amount must be positive!')
            self.__balance -= withdrawal_amount
        except ValueError:
            print('\nInput must be a number!')

    def deposit(self):
        """
        deposits the account from account, unless:
        - deposit amount is negative or not a number, then raises a ValueError correspondingly.
        """
        try:
            deposit_amount = float(input('\nEnter deposit amount: '))
            if deposit_amount < 0:
                raise ValueError('Deposit amount must be positive!')
            self.__balance += deposit_amount
        except ValueError:
            print('\nInput must be a number!')

    def change_password(self):
        """
        changes the password for the account. unless:
        - new password is the same as old one, then prints that password is the same.
        """
        new_password = input('\nEnter New Password: ')
        if new_password == self.__password:
            print('\nPassword is the same!')
        else:
            self.__password = new_password
            print('\nPassword changed successfully!')

    def save_account_to_config(self, file_path):
        """
        saves the account to the config file using the dump_to_json from utils.py.
        """
        account_data = {
            'password': self.__password,
            'balance': self.__balance,
        }
        accounts = load_json_file(file_path)
        accounts[self.account_number] = account_data
        dump_to_json(file_path, accounts)

    @classmethod
    def load_account(cls, file_path):
        """
        gets account number and password from user, and returns a new cls(parameters) object, unless:
        - account number isn't in config, then raises a ValueError correspondingly.
        and if account number was in config:
        - if account password is wrong, raises a ValueError correspondingly.
        """
        try:
            account_number = input("\nEnter account number: ")
            account = load_json_file(file_path).get(account_number)
            if account is None:
                raise ValueError('\nAccount does not exist!')
            account_password = input("\nEnter password: ")
            if account['password'] != account_password:
                raise ValueError('\nIncorrect password!')
            return cls(account_number, account_password, account['balance'])
        except ValueError as error:
            print(error)
            raise


# Method Factories:
def get_startup_method():
    """
    Method factory for the startup menu choices.
    """
    return {
        '1': start_action_loop,
        '2': lambda *_: exit_program(),
    }


def get_action_method(account, file_path):
    """
    Method factory for the action menu choices.
    """
    return {
        '1': account.print_balance,
        '2': account.withdraw,
        '3': account.deposit,
        '4': account.change_password,
        '5': lambda: account.save_account_to_config(file_path)
    }


# User choices from menus:
def get_startup_choice():
    """
    Shows startup choice menu and gets user choice.
    """
    return input('\nWelcome! Here are your options:\n\n'
                 '[1] Log-in\n'
                 '[2] Exit out of program\n'
                 'Enter your choice: ')


def get_user_action():
    """
    Shows banking action choice menu and gets user choice.
    """
    return input('\n Choose an option:\n'
                 '[1] Check Balance\n'
                 '[2] Make a withdrawal\n'
                 '[3] Make a deposit\n'
                 '[4] Change password\n'
                 '[5] Save & Exit\n'
                 'Enter your choice: ')


# Main program loop functions:
def start_action_loop(cls, file_path):
    """
    Uses load_account method, then inside a loop uses get_user_action function to get user choice,
    performs the action using the method factory, unless:
    - Input isn't one of the choices, then raises a ValueError correspondingly.
        * for input 5 (save & exit), also break the loop after method is done.
    """
    print("\nLogging in...")
    account = cls.load_account(file_path)
    action_methods = get_action_method(account, file_path)

    while True:
        choice = get_user_action()
        action = action_methods.get(choice)
        if action:
            try:
                action()
            except ValueError as error:
                print(error)
                raise
            if choice == '5':
                break
        else:
            print('\nInvalid input, please try again!')


def exit_program():
    """
    print "Exiting program..." and exit the program.
    """
    print('\nExiting program...')
    exit()


def start_program_loop(cls, file_path):
    """
    Basically the function that encases the whole program's functionality.
    gets the user choice, performs the startup action using the method factory,
    if choice is 2: exits program using the exit_program function.
    if choice is 1: run the start_action_loop function that enters the action menu.
    if choice is invalid, raises a ValueError correspondingly.
    """
    startup_methods = get_startup_method()
    while True:
        try:
            choice = get_startup_choice()
            action = startup_methods.get(choice)
            if action:
                action(cls, file_path)
            else:
                print('\nInvalid input, please try again!')
        except ValueError as error:
            continue


# Use the program with Account as the class and CONFIG_FILE_PATH as config directory.
start_program_loop(Account, CONFIG_FILE_PATH)
