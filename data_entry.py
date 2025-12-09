# serves all functions that will extract input from the user

from datetime import datetime

# CATEGORIES = dict that will serve as a check for the input in category fn.
CATEGORIES = {
    'I': 'Income',
    'E': 'Expenses'
}

# prompt = serves as the input for the user before asking for date. This will allow this fn to be dynamic

# allow_default = used to input current date if user does not input a date.
def get_date(prompt, allow_default = False):
    date_str = prompt
    if allow_default and not date_str: # user did not enter date
        # create a date as current date. 
        # strftime =  formats str to datetime
        converted_date = datetime.today().strftime("%d-%m-%Y")
        print(f'Date today: {converted_date}')
        return converted_date
    try:
        # create a valid date from the input by parsing a string (date_str) to a valid time(strptime()).
        valid_date = datetime.strptime(date_str, '%d-%m-%Y')
        print(f'You entered a valid date: {valid_date}')
        return valid_date.strftime('%d-%m-%Y')
       
    except ValueError as err:
        print('Entered date is not valid. Format should be: dd/mm/YYYY') 
        print(err) 
        #recursive function to call if invalid date
        prompt = input('Enter a valid date: ')
        return get_date(prompt, allow_default)
        

def get_amount():
    try:
        amount = float(input('Enter amount: '))
        if amount <= 0:
            raise ValueError('Amount cannot be less than or 0.')
        return f'{amount:.2f}' # display float with 2 decimal places
    except ValueError:
        print('Amount must be greater than 0')
        return get_amount()


def category():
    category = input('Enter "I" form income or "E" for expense: ').upper()
    if category in CATEGORIES:
        if category == 'I':
            print(f'Selected {CATEGORIES[category]}' )
        elif category == 'E':
            print(f'Selected {CATEGORIES[category]}' )
        return CATEGORIES[category]
    print('Not a valid category. Enter "I" for Income or "E" for Expense')
    # recursive function to call the fn in case of error.
    return category()

def get_description():
    return input('Enter your description (optional): ')

# get_date('')
# get_date('12-12-1212')
# print(get_amount())
# print(category())
# get_description()


