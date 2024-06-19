logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(argument1, argument2):
    return argument1 + argument2

def subtract(argument1, argument2):
    return argument1 - argument2

def multiply(argument1, argument2):
    return argument1 * argument2

def divide(argument1, argument2):
    return argument1 / argument2

operations_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    print(logo)
    argument1 = input('What\'s the first number?: ')
    argument1 = float(argument1) if '.' in argument1 else int(argument1)
    for operation in operations_dict.keys():
        print(operation)
    should_continue = True
    while should_continue:
        operation_symbol = input('Pick an operation: ')
        argument2 = input('What\'s the next number?: ')
        argument2 = float(argument2)  if '.' in argument2 else int(argument2)
        calc_function = operations_dict[operation_symbol]
        answer = calc_function(argument1, argument2)
        print(f'{argument1} {operation_symbol} {argument2} = {answer}')
        flag = input(
            f'Type "y" to continue calculations with {answer}. '
            'Type "n" to exit: '
        ).lower()
        while flag not in ['y', 'n']:
            flag = input(
                'You\'ve typed a wrong letter. Choose "y" or "n": '
            ).lower()
        if flag == 'y':
            argument1 = answer
        else:
            should_continue = False
            calculator()

calculator()