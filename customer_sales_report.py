import csv
import os

NEW_FILE = "salesreport.csv"
CSV_FILE = "sales.csv"

def main():
    infile = open(CSV_FILE, "r", newline='')
    reader = csv.reader(infile)
    next(reader)
    
    outfile = open(NEW_FILE, "w", newline='')
    writer = csv.writer(outfile)
    writer.writerow(["Customer" , "Total"])
    last_customer = ""
    count = 0
    total = 0


    for row in reader:
        if count == 0:
            last_customer = row[0]
        if row[0] == last_customer:
            total += float(row[3]) - (float(row[4]) + float(row[5]))
            
        else:
            writer.writerow([last_customer, format(total , '.2f')])

            total = float(row[3]) - (float(row[4]) + float(row[5]))
            
        last_customer = row[0]
        count += 1
    writer.writerow([last_customer, format(total , '.2f')])

   
    infile.close()
    outfile.close()

main()