from random import randint
while input('Press q to quit')!='q':
    randomNo = randint(0,100) 
    userInput = input("Guess a number")
    if (randomNo == userInput):
        print('You guessed right!!')
    else:
        print('naaa wrong!')
                
                
                
