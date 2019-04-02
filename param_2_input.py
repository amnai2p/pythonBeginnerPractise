a = input("Type a number")
b = input("Type another number")    
a = int(a)
b = int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero. try again")
    
