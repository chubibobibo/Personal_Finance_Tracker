import pandas as pd
import csv #allows to load csv file that serves as a database.
from datetime import datetime

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


# Test creating a reading/initializing a csv file
CSV.initialize_csv()
CSV.add_entry('10/12/24', 63, 'debit', 'test description')
CSV.add_entry('11/12/24', 63, 'credit', 'test description')
CSV.add_entry('12/12/24', 63, 'debit', 'test description')
            

