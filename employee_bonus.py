import os
import csv

CSV_FILE = "EmployeePay.csv"

def main():
    infile = open(CSV_FILE, "r", newline='')
    reader = csv.reader(infile)
    next(reader)

    for row in reader:
        print("ID:         " + row[0])
        print("First Name: " + row[1])
        print("Last Name:  " + row[2])
        print("Salary:     " + row[3])
        print("Bonus:      " + row[4])
        print("_____________________________")
        
        
        
        
    infile.close()

main()