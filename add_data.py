from employee import Employee
from database_management import *
print("result =>>>", show_all())
def get_emp_info():
    first_name = input("Enter first name: ").capitalize()
    last_name = input("Enter last name: ").capitalize()
    pay = int(input("Enter your pay in numbers: "))
    return first_name, last_name, pay

first_name, last_name, pay = get_emp_info()
emp = Employee(first_name, last_name, pay)

insert_emp(emp)

# emps = get_emps_by_name('Doe')
# print(emps)
#
# update_pay(emp, 95000)
# remove_emp(emp)

# emps = get_emps_by_name('Doe')
# print(emps)
print("result =>>>", show_all())
emp = {'first':'Test', 'last':'Test', 'pay':123}
remove_emp(emp)
print("result =>>>", show_all())

conn.close()