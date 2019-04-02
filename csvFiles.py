import csv
with open('newcsv2.csv','w') as csvFile:
    spamwriter = csv.writer(csvFile,delimiter = ',')
    spamwriter.writerow(['One','Two','Three','hello'])
    spamwriter.writerow(['Four','five','six'])
