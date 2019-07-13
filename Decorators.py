''' Decorators in Python '''



# from functools import wraps

# DECORATOR 'decoratore' starts

def caps_lock(funzione_parametro) :

    b = funzione_parametro()
    #@wraps(funzione_parametro)
    def wrapper() :

        print("\n")

        print ("\n")
        print(" ************************************************************* \n ")
        print("\n")
        print(" " + b + "\n")
        # " ******************** "
        print("\n")
        print(" ************************************************************* \n")
        print("\n")
        # funzione_parametro().upper()
        # funzione_parametro

    return wrapper()

# DECORATOR 'decoratore' ends




# FUNCTION 'esempio' starts

@caps_lock
def esempio () :
    a=input("Type something here : ")
    return a.upper()

# FUNCTION ' esempio' ends



# print("\n")
# bprint(" The original function is \n")
print("\n")
esempio
print("\n")
# print(a)
# print("\n")
# decoratore(esempio)
# print(esempio.__name__)

"""
print("\n")
print(" The decorated original function is \n")
print("\n")
decoratore(esempio)
"""

 

 

 
