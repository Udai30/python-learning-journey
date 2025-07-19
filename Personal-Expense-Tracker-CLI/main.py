# Importing Dependencies
from datetime import datetime
import csv
import os
from collections import deque

# Blueprints
categories = {
    'default': [
        'Food', 'Transport', 'Utilities', 'Entertainment',
        'Healthcare', 'Shopping', 'Education', 'Bills',
        'Rent', 'Groceries', 'Fuel', 'Miscellaneous'
    ],
    'custom': []  # User can add up to 5 custom categories
}

expense_template = {
    'id': None,           # Will be filled with actual ID (auto)
    'amount': 0.0,        # Will be filled with actual amount
    'date': '',           # Will be filled with actual date (auto)
    'time': '',           # Will be filled with actual time (auto)
    'type': '',           # Will be either income or expense
    'category': '',       # Will be filled with actual category
    'description': '',    # Will be filled with actual description
    'payment_method': ''  # Will be filled with actual method
}

id = 1

# Initialize CSV
def initialize_csv():
    if not os.path.exists('transactions.csv'):
        with open('transactions.csv', mode='w') as csv_file:
            fieldnames = expense_template.keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

# Next Id
def next_id():
    global id
    last_row = None
    with open('transactions.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            last_row = row
        if last_row:
            id = int(last_row['id']) + 1
    return id

# New Transaction
def transaction():
    global id
    initialize_csv()

    new = dict.fromkeys(expense_template.keys())

    new['id'] = next_id()


    date = datetime.today().strftime('%d/%m/%Y')
    new['date'] = date

    time = datetime.now().strftime('%H:%M:%S')
    new['time'] = time

    amt = input("Amount: ")
    new['amount'] = float(amt)

    trns_type = input("Is the transaction an income or expense?: ")
    new['type'] = trns_type

    category = input("Category: ")
    new['category'] = category

    description = input("Description: ")
    new['description'] = description

    payment_method = input("Payment method: ")
    new['payment_method'] = payment_method

    with open('transactions.csv', mode='a', newline='') as csv_file:
        fieldnames = expense_template.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(new)

    return new

# View Transactions
def view_transation(last):
    with open('transactions.csv', mode='r') as csv_file:
        last_n_rows = deque(csv.reader(csv_file), last)

        for row in last_n_rows:
            print(row)


# Main Function
def main():
    run = input("Do you want to run the transaction? (y/n): ")

    if run == 'y':
        print(transaction())
    else:
        views = input("Do you want to view the transactions? (y/n): ")
        if views == 'y':
            last = int(input("How many transactions do you want to view?: "))
            view_transation(last)

if __name__ == "__main__":
    main()