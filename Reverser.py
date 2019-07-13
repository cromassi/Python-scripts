'''   Reverser

      This is a function to which you will pass a string as a parameter

      will return you a version of the same string in reverse

      (eg "abcd" becomes "dcba") '''






# FUNCTION 'inverti_stringa' starts

def inverti_stringa(string) :
    l=len(string)
    inv_string=""


    for i in range(l-1, 0, -1) :
        inv_string += string[i]
    inv_string += string[0]

    print("\n")
    print("The reverse of the original string is " + " '" + inv_string + "' ")
    print("\n")

    return inv_string

# FUNCTION 'inverti_stringa' ends







"""

# FUNCTION 'inverti_stringa' starts

def inverti_stringa(string) :
    i=len(string)-1
    inv_string=""


    while i >= 0 :
        inv_string += string[i]
    i -= 1

    print("\n")
    print("The reverse of the original string is " + " '" + inv_string + "' ")
    print("\n")

# FUNCTION 'inverti_stringa' ends


"""





while True :

    print("\n")
    print("Welcome to this simple software to reverse an orignal alphanumerical text string")
    print("\n")
    s=input(" Please type here the original text string : ")
    print("\n")


    inverti_stringa(s)


    p = input("Do you want to use this software again ? (y/n) ")

    while p != "y" and p != "n" and p != "Y" and p != "N":
        print("\n")
        print(" Sorry, you have to type 'y' or 'Y' for reversing another text string otherwise 'n' or 'N' for stopping this software : ")
        p = input("Do you want to continue using this software ? (y/n) ")

    if p == "y" or p == "Y":
        continue
    elif p == "n" or p == "N":
        print("\n")
        print("Thanks for using this software, bye bye ")
        break
