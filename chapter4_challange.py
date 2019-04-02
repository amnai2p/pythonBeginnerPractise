def add():
    """
      Returns age of the person.
          Take input from user
          if less than zero then ask again
          :return : int age of the person
    """
    age = input("whats your age")
    age = int(age)
    if(age > 0):
        return age
    else:
        return add()           
        

print(add())
