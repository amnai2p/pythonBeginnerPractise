mylist = list()
with open('/var/www/html/python/myFile.txt','r') as myFile:
                for line in myFile.read():
                                mylist.append(line)
                print(mylist)                
                                
