# Importing Dependencies
from datetime import datetime

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

# New Transaction
def transaction():
    new = dict.fromkeys(expense_template.keys())

    new['id'] = id
    id += 1

    date = datetime.today().strftime('%d/%m/%Y')
    new['date'] = date

    time = datetime.now().strftime('%H:%M:%S')
    new['time'] = time

    amt = input("Amount: ")
    new['amount'] = float(amt)

    type = input("Is the transaction an income or expense?: ")
    new['type'] = type

    category = input("Category: ")
    new['category'] = category

    description = input("Description: ")
    new['description'] = description

    payment_method = input("Payment method: ")
    new['payment_method'] = payment_method

    return new
    return id


def main():
    run = input("Do you want to run the transaction? (y/n): ")

    if run == 'y':
        print(transaction())

if __name__ == "__main__":
    main()