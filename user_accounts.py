from ConcludingExcersize.utils import dump_to_json
from utils import load_json_file
from account import Account


class UserAccounts:
    def __init__(self, accounts: list[Account]):
        """
        defines an accounts list containing each account in the config as an Account class.
        """
        self.accounts = accounts
        self.account_numbers = [account.account_number for account in self.accounts]

    def dump_accounts_to_file(self, file_path):
        """
        creates a dict containing {account number: {'password': password, 'balance': balance}}
        for each account in self.accounts and dumps it to json file.
        """
        account_values = {account.account_number: {'password': account.password, 'balance': account.balance}
                          for account in self.accounts}
        dump_to_json(file_path, account_values)

    def create_new_account(self):
        """
        asks for new account number, and checks if it already exists. if not, creates a new account
        and asks for password, adds it to the accounts list.
        """
        account_number = input("\nEnter new account number: ")
        if account_number in self.account_numbers:
            raise ValueError("\nAccount already exists!")
        account_password = input("\nEnter new account password: ")
        account = Account(account_number, account_password)
        self.accounts.append(account)

    def log_into_account(self):
        """
        asks for new account number, and checks if it exists, if it does, asks for password, and if it's
        correct returns the account as an Account class.
        """
        account_number = input("\nEnter account number: ")
        try:
            account = next((account for account in self.accounts if account.account_number == account_number))
        except StopIteration:
            raise ValueError("\nAccount does not exist!")
        account_password = input("\nEnter password: ")
        if account_password != account.password:
            raise ValueError('Incorrect password!')
        return account

    @classmethod
    def get_accounts_from_file(cls, file_path):
        accounts = [Account(account_number, data['password'], data['balance'])
                    for account_number, data in load_json_file(file_path).items()]
        return cls(accounts)
