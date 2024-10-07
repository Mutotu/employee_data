import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')
# this resets the database
conn = sqlite3.connect(':memory:')
c = conn.cursor()
# Create a table and comment it out
#  or using connect(':memory:') no need to comment it out
c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")
##### doing it this way creates a security prob;em. SQL injection instead
# c.execute("INSERT INTO employees VALUES ('{}', '{}', '{}')".format())
#####  instead do this
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees VALUES (:first, :last, :pay", {'first':emp_2.first, 'last': emp_2.last,'pay': emp_2.pay})
# c.execute("INSERT INTO employees VALUES ('Sam', 'Tan', 6000)")
# conn.commit()
# c.execute("SELECT * FROM employees")
# print(c.fetchall())
######
emp_1 = Employee('John', 'Doe', 90000)
emp_2 = Employee('JSam', 'Doaae', 30000)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
c.execute("SELECT * FROM employees")
# c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
# c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
print(c.fetchall())
conn.commit()

conn.close()