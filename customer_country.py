import csv
import os

NEW_FILE = "customer_country.csv"
CSV_FILE = "customers.csv"

def main():
    infile = open(CSV_FILE, "r", newline='')
    reader = csv.reader(infile)
    next(reader)
    
    outfile = open(NEW_FILE, "w", newline='')
    writer = csv.writer(outfile)
    writer.writerow(["First Name" , "Last Name" , "Country"])

    cust_info = []

    for row in reader:
        cust_info = [row[1], row[2], row[4]]
        writer.writerow(cust_info)

    infile.close()
    outfile.close()





main()

