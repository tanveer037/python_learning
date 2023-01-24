from os import chdir
from csv import reader, DictReader
chdir("""/mnt/d/Tanveer's profile/Lessons/The Modern Python 3 Bootcamp/[TutsNode.com] - The Modern Python 3 Bootcamp/31 - Working With CSV and Pickling""")


with open('1 - fighters.csv') as f:
    rows = reader(f)
    # next(rows)
    for row in rows:
        # print(f"{row[0]} is from {row[1]}")
        print(row)


print('\n')

with open('1 - fighters.csv') as f:
    columns = DictReader(f)
    for column in columns:
        # print(column['Name'])
        print(column)