# serves all functions that will extract input from the user

from datetime import datetime

# prompt = serves as the input for the user before asking for date. This will allow this fn to be dynamic

# allow_default = used to input current date if user does not input a date.
def get_date(prompt, allow_default = False):
    date_str = input(prompt) # Takes the value of date_str from the argument passed as prompt
    # print(isinstance(date_str, str))
    print(date_str)
    if allow_default and not date_str: # user did not enter date
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
        # prompt = input('Enter a correct date: ')
        return get_date(prompt, allow_default)
        

def get_amount():
    pass

def category():
    pass

def get_description():
    pass

# get_date('')
get_date('haha')


