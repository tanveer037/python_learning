from os import chdir
from csv import writer, reader
chdir('/mnt/d/Codes/python_learning/problems')


def add_user(first_name, last_name):
    with open('users.csv', 'a') as f1:
        csv_writer = writer(f1)
        csv_writer.writerow([first_name, last_name])


def print_users():
    with open('users.csv') as f1:
        csv_reader = reader(f1)
        next(csv_reader)
        for item in csv_reader:
            print(item[0] + " " + item[1])


def find_user(first_name, last_name):
    with open('users.csv') as f1:
        csv_reader = reader(f1)
        next(csv_reader)
        list_of_readers = list(csv_reader)
        if [first_name, last_name] in list_of_readers:
            return (list_of_readers.index([first_name, last_name]))
        return f"{first_name} {last_name} not here"


# add_user('Tanveer','Tayeb')
# add_user('Asib','Ahmed')
# print_users()
# print(find_user('Asib','Ahmed'))
