"""Lab Exercise 3: CSV-Based Payroll Management System
Question
Develop a Python program to create a simple payroll management system using the CSV module.

The program should:
1. Accept employee details such as Employee ID, Name, Basic Salary, Allowance and Deduction.
2. Calculate the net salary of each employee.
3. Store all employee details in a CSV file named payroll.csv.
4. Read the CSV file and display all employee payroll records.
Use the following formula:
Net Salary = Basic Salary + Allowance - Deduction"""

import csv

try:
    n = int(input("Enter number of employees: "))

    with open("payroll.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Employee ID", "Name", "Basic Salary",
                         "Allowance", "Deduction", "Net Salary"])

        for i in range(n):
            print("\nEnter Employee Details:")
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            basic = float(input("Enter Basic Salary: "))
            allowance = float(input("Enter Allowance: "))
            deduction = float(input("Enter Deduction: "))

            net_salary = basic + allowance - deduction

            writer.writerow([emp_id, name, basic, allowance,
                             deduction, net_salary])

    print("\nPayroll Records:")

    with open("payroll.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except ValueError:
    print("Please enter valid numeric values.")

