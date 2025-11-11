import sys,os
from colorama import Fore

def display_menu():
    print(Fore.GREEN + """
    1: OP-Tool (Hacking Tools)      | 2: Paid-Tools
    3: Info (about-us)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python OP-Tool/OP-Tool.py"' if os.name == 'nt' else 'python OP-Tool/OP-Tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')

    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
