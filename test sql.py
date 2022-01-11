import sqlite3
from contextlib import closing
value = ''
f = "f"
count = 0
con = 'orders.db'

with closing(sqlite3.connect(con)) as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
                    select * from testing
                    """)
    sql = cursor.fetchall()
for i in sql:
    value_output = i['output']
    value = i['input']
    count = 0
    f = 'f'
    for j in range(len(value)):
        if f == value[j]:
            count += 1
    if count == 1:
        s = value.find(f)
        if value_output == str(s):
            print('TRUE')
    elif count > 1:
        if str(value.find(f)) in value_output and str(value.rfind(f)) in value_output:
            print('TRUE')
    else:
        s = 'NO'
        if value_output == s:
            print('TRUE')
