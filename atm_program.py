from user_accounts import UserAccounts
from utils import exit_program

ACCOUNTS_INFO_FILE_PATH = 'accounts_info.json'


def get_startup_action(user_accounts, file_path):
    """
    Method factory for the startup menu choices.
    """
    return {
        '1': lambda: start_action_loop(user_accounts, file_path),
        '2': exit_program,
        '3': user_accounts.create_new_account
    }


def get_startup_choice():
    """
    returns the user's startup menu input, after checking that it's a valid choice.
    """
    choice = input('\nWelcome! Here are your options:\n'
                   '[1] Log-in\n'
                   '[2] Exit out of program\n'
                   '[3] Create a new account\n'
                   'Enter your choice: ')
    if choice not in ['1', '2', '3']:
        raise ValueError('\nInvalid choice!')
    return choice


def get_user_action():
    """
    returns the user's action menu input, after checking that it's a valid choice.
    """
    choice = input('\n Choose an option:\n'
                   '[1] Check Balance\n'
                   '[2] Make a withdrawal\n'
                   '[3] Make a deposit\n'
                   '[4] Change password\n'
                   '[5] Save & Exit\n'
                   'Enter your choice: ')
    if choice not in ['1', '2', '3', '4', '5']:
        raise ValueError('\nInvalid choice!')
    return choice


def start_action_loop(user_accounts, file_path):
    """
    asks for the account number and password, if correct brings the user to the action menu and performs the action for
    each input. if choice was 5 then saves the accounts to the file and breaks the loop.
    """
    print("\nLogging in...")
    try:
        account = user_accounts.log_into_account()
    except ValueError as e:
        print(e)
        return
    while True:
        try:
            choice = get_user_action()
        except ValueError as e:
            print(e)
            continue
        if choice == '5':
            print('\nSaving and exiting...')
            user_accounts.dump_accounts_to_file(file_path)
            break
        try:
            account.get_user_actions.get(choice)()
        except ValueError as e:
            print(e)


def start_program_loop(user_accounts, file_path):
    """
    gets the input from the startup menu and performs the action for the choice.
    """
    if __name__ == "__main__":
        while True:
            try:
                choice = get_startup_choice()
            except ValueError as e:
                print(e)
                continue
            try:
                get_startup_action(user_accounts, file_path).get(choice)()
            except ValueError as e:
                print(e)


start_program_loop(UserAccounts.get_accounts_from_file(ACCOUNTS_INFO_FILE_PATH), ACCOUNTS_INFO_FILE_PATH)
