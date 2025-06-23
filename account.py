class Account:
    """
    class for a bank account that has an account number, password and balance, and has methods that:
    return the password, prints the balance, withdraws and deposits from balance, change the password, get teh account's
    data and a method dictionary that contains the methods used by the main program.
    """

    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.__password = password
        self.__balance = balance

    def __eq__(self, other):
        return self.account_number == other.account_number

    def __hash__(self):
        return hash(self.account_number)

    def get_password(self):
        return self.__password

    def print_balance(self):
        print(f'\nYour balance is: {self.__balance}')

    def withdraw(self):
        """
        asks for withdrawal amount, checks that it's not negative, is a number and not bigger then the account's balance,
        then subtracts it from the balance.
        """
        try:
            withdrawal_amount = float(input('\nEnter Withdrawal amount: '))
        except ValueError:
            raise ValueError('Input must be a number!')
        if withdrawal_amount > self.__balance:
            print('Not enough balance!')
            raise ValueError
        if withdrawal_amount < 0:
            print('Withdrawal amount must be positive!')
            raise ValueError
        self.__balance -= withdrawal_amount

    def deposit(self):
        """
        asks for deposit amount, checks that it's not negative and is a number, then adds it to the account's balance.
        """
        try:
            deposit_amount = float(input('\nEnter deposit amount: '))
        except ValueError:
            print('Input must be a number!')
            raise ValueError
        if deposit_amount < 0:
            print('Deposit amount must be positive!')
            raise ValueError
        self.__balance += deposit_amount

    def change_password(self):
        """
        asks for a new password, checks that it's not the same as the old password, and changes it.
        """
        new_password = input('\nEnter New Password: ')
        if new_password == self.__password:
            print('\nPassword is the same!')
        else:
            self.__password = new_password
            print('\nPassword changed successfully!')

    def get_account_data(self):
        account_values = {
            'password': self.__password,
            'balance': self.__balance
        }
        return self.account_number, account_values

    def get_action_method(self, user_accounts, file_path):
        """
        dictionary containing the methods performed by the main program's action menu
        """
        from useraccounts import UserAccounts
        return {
            '1': self.print_balance,
            '2': self.withdraw,
            '3': self.deposit,
            '4': self.change_password,
            '5': lambda: user_accounts.dump_accounts_to_config()
        }
