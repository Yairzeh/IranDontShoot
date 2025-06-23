from useraccounts import UserAccounts

CONFIG_FILE_PATH = 'config.json'


def get_startup_method(user_accounts, file_path):
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
    choice = input('\nWelcome! Here are your options:\n\n'
                   '[1] Log-in\n'
                   '[2] Exit out of program\n'
                   '[3] Create a new account\n'
                   'Enter your choice: ')
    if choice not in ['1', '2', '3']:
        print('Invalid choice!')
        raise ValueError
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
        print('Invalid choice!')
        raise ValueError
    return choice


def start_action_loop(user_accounts, file_path):
    """
    asks for the account number and password, if correct brings the user to the action menu and performs the action for
    each input.
    """
    print("\nLogging in...")
    try:
        account = user_accounts.load_account()
    except ValueError:
        return
    while True:
        try:
            choice = get_user_action()
        except ValueError:
            continue
        account.get_action_method(user_accounts, file_path).get(choice)()
        if choice == '5':
            break


def exit_program():
    print('\nExiting program...')
    exit()


def start_program_loop(user_accounts, file_path):
    """
    gets the input from the startup menu and performs the action for the choice.
    """
    if __name__ == "__main__":
        while True:
            try:
                choice = get_startup_choice()
            except ValueError:
                continue
            get_startup_method(user_accounts, file_path).get(choice)()


start_program_loop(UserAccounts(CONFIG_FILE_PATH), CONFIG_FILE_PATH)
