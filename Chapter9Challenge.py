user_input = input('Please provide data to save \n')
with open('userData.txt','a+') as userDataFile:
    userDataFile.write(user_input +'\r')
