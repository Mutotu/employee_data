import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    # Check if emp is a dictionary or an Employee object
    if isinstance(emp, dict):
        first = emp['first']
        last = emp['last']
    else:
        first = emp.first
        last = emp.last

    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': first, 'last': last})

def show_all():
    c.execute("SELECT * FROM employees")
    return c.fetchall()

# conn.close()