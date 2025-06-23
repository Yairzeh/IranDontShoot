from utils import load_json_file, load_and_dump_to_json
from account import Account


class UserAccounts:
    def __init__(self, file_path):
        """
        defines an accounts list containing each account in the config as an Account class.
        """
        self.file_path = file_path
        self.__accounts = [Account(account_number, data['password'], data['balance'])
                           for account_number, data in load_json_file(file_path).items()]

    def dump_accounts_to_config(self):
        """
        dumps all accounts into the config file.
        """
        for account in self.__accounts:
            load_and_dump_to_json(self.file_path, account.get_account_data()[0], account.get_account_data()[1])

    def create_new_account(self):
        """
        asks for new account number, and checks if it already exists. if not, creates a new account
        and asks for password, adds it to the accounts list and dumps the list into the config file.
        """
        account_number = input("\nEnter new account number: ")
        if Account(account_number, None, None) in self.__accounts:
            print("\nAccount already exists!")
            raise ValueError
        account_password = input("\nEnter new account password: ")
        account = Account(account_number, account_password)
        self.__accounts.append(account)
        self.dump_accounts_to_config()

    def load_account(self):
        """
        asks for new account number, and checks if it exists in the config, if it does, asks for password, and if it's
        correct returns the account as an Account class.
        """
        account_number = input("\nEnter account number: ")
        if Account(account_number, None, None) not in self.__accounts:
            print('Account does not exist!')
            raise ValueError
        account = self.__accounts[self.__accounts.index(Account(account_number, None, None))]
        account_password = input("\nEnter password: ")
        if account_password != account.get_password():
            print('Incorrect password!')
            raise ValueError
        return account
