class Account:
    """
    class for a bank account that has an account number, password and balance, and has methods that:
    print the balance, withdraw and deposit from balance, change the password 
    and a method factory that contains the user's actions.
    """

    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.withdraw = 'withdrawal'
        self.deposit = 'deposit'

    def __eq__(self, other):
        return self.account_number == other.account_number

    def __hash__(self):
        return hash(self.account_number)

    def print_balance(self):
        print(f'\nYour balance is: {self.balance}')

    def withdraw_or_deposit(self, action):
        """
        checks that action is either deposit or withdraw, then that the inputted amount is positive and a number, 
        if it's a deposit, adds it to balance. if it's a withdrawal, checks that the amount is smaller the balance,
        then subtracts it from the balance.
        """
        if action in [self.withdraw, self.deposit]:
            try:
                amount = float(input(f'\nEnter {action} amount: '))
            except ValueError:
                raise ValueError('\nInput must be a number!')
            if amount < 0:
                raise ValueError(f'\n{action} amount must be positive!')
            if action == self.withdraw:
                if amount > self.balance:
                    raise ValueError('\nNot enough balance!')
                self.balance -= amount
            if action == self.deposit:
                self.balance += amount
            return
        raise ValueError('Invalid action!')

    def change_password(self):
        """
        asks for a new password, checks that it's not the same as the old password, and changes it.
        """
        new_password = input('\nEnter New Password: ')
        if new_password == self.password:
            print('\nPassword is the same!')
        else:
            self.password = new_password
            print('\nPassword changed successfully!')

    @property
    def get_user_actions(self):
        return {
            '1': self.print_balance,
            '2': lambda: self.withdraw_or_deposit(self.withdraw),
            '3': lambda: self.withdraw_or_deposit(self.deposit),
            '4': self.change_password,
        }
