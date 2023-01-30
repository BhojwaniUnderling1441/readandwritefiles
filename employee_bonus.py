import os
import csv

CSV_FILE = "EmployeePay.csv"

def main():
    infile = open(CSV_FILE, "r", newline='')
    reader = csv.reader(infile)
    next(reader)
    
    print("ID | First Name | Last Name | Salary | Bonus")

    for row in reader:
        print(row)
        
    infile.close()

main()