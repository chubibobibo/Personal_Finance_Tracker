import pandas as pd
import csv #allows to load csv file that serves as a database.
from datetime import datetime
from data_entry import get_date, get_amount, get_description, category

# allows to work easily for csv file
class CSV:
    #class attributes
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']

    # method to initialize csv file (create if not existing yet)
    # class method will only allow access to the class (meaning other class methods and attribtues) and not with class instances.
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # create a CSV file if does not exist
            # using Data frame, create the the column headers of the data file
            df = pd.DataFrame(columns=cls.COLUMNS)
            # export the df(created data frame) to a CSV file (class attribute)
            df.to_csv(cls.CSV_FILE, index=False)
    
    # create a class method that will add an entry to the csv file (for the columns that we specified)
    @classmethod
    def add_entry(cls, date, amount, category, description):
        # dict that we will use to write as rows using DictWriter()
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        # context manager ("with - as" syntax )
            # -opens the CSV_FILE and store it to csv_entry variable
            # -context manager will handle automatically closing the file as soon as the code inside it is done executing, thus preventing any memory leaks cleaning everyting.
            # -It is recommended to use context manager when dealing with reading/managing files.
            # -'a' stands for append mode
        with open (cls.CSV_FILE, 'a', newline='') as csv_entry:
            writer = csv.DictWriter(csv_entry, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print('Entry added successfully')

    @classmethod
    def get_transactions(cls,start_date, end_date):
        # read csv_file
        df = pd.read_csv(cls.CSV_FILE)
        #convert date columns in the csv file to date-time objects that will allow us to query it
        df['date'] = pd.to_datetime(df['date'], format = '%d-%m-%Y')
        # parse the text input and convert date input to a valid date time
        start_date = datetime.strptime(start_date, '%d-%m-%Y')
        end_date = datetime.strptime(end_date, '%d-%m-%Y')
        # mask = querying the different rows with a start and end date
        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        # df.loc = selects rows and columns not by position but by labels
        filtered_date = df.loc[mask] # returns a new data frame that contains row where mask is applied

        if filtered_date.empty:
            print('There are no results')
        else:
            print(f'Transactions from {start_date.strftime('%d-%m-%Y')} to {end_date.strftime("%d-%m-%Y")}')
            # formatters = specify specific columns to format
            # lambda function to format all elements inside the filtered column
            print(filtered_date.to_string(index=False, formatters={'date': lambda x: x.strftime('%d-%m-%Y')}))

            # find the total income
            # filter category having category as "Income". second query "amount" should wrap around the first query/mask
            # sum() to total all elements in the column.
            total_income = filtered_date[filtered_date['category'] == 'Income']['amount'].sum()
            total_expense = filtered_date[filtered_date['category'] == 'Expense']['amount'].sum()
            print('\nSummary:')
            print(f'Total Income: {total_income}')
            print(f'Total Expense: {total_expense}')
        return filtered_date



is_running = True
def add():
    # initialize csv file using the classmethod initialize_csv
    CSV.initialize_csv()
    response_date = input('Enter the date of the transaction (dd-mm-yyyy): ')
    input_date = get_date(response_date, allow_default=True)
    input_amount = amount = get_amount()
    print(amount)
    input_category = category()
    input_description = get_description()
    CSV.add_entry(input_date, input_amount, input_category, input_description)


def main():
    while is_running == True:
        print('**********************')
        print('Select your transaction type')
        print('1. Add Transaction')
        print('2.View transactions and summary withing date range')
        print('1. Exit')
        print('**********************')

        choice = input('Select your transaction type: ')
        if choice == '1':
            add()
        elif choice == '2':
            start_date = input('Enter your start date: ')
            end_date = input('Enter your end date: ')
            CSV.get_transactions(start_date, end_date)
        elif choice == '3':
            print('Thank you for using the app')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()






# Test creating a reading/initializing a csv file
# CSV.initialize_csv()
# CSV.add_entry('10/12/24', 63, 'debit', 'test description')
# CSV.add_entry('11/12/24', 63, 'credit', 'test description')
# CSV.add_entry('12/12/24', 63, 'debit', 'test description')
# get_date('12-12-1212')

# add()
print(CSV.get_transactions( '03-11-2025', '08-12-2025'))

            

