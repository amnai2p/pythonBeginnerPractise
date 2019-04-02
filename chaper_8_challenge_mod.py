from random import randint
def getrand():
    print(randint(0,100))
def askmyName():
    name = input('what is your name')
    print('your name is {}'.format(name))
def showmetrick():
    for i in range(0,10):
        mystars = i            
        while mystars !=0:
            stars +='*'
            mystars -= 1
        print(stars)
        i +=  1
                        
                
