import csv
with open('newcsv2.csv','r') as csvFile:
    spamereader = csv.reader(csvFile,delimiter=',')
    for row in spamereader:
        print(','.join(row))
