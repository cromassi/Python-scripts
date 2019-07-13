
''' Unstoppable Summaster.

     Write a "sum" function that adds all the elements together

     of a list of numbers. '''







# FUNCTION 'sommatrice' starts

def sommatrice(list):
    print("\n")
    print("The list of numer you typed is \n")
    print(list)
    lunghezza = len(list)
    sum = 0

    for i in range(0, lunghezza):
        sum += float(list[i])

    print("\n")
    print("The sum of all numbers in the list is " + str(sum))


# FUNCTION 'sommatrice' ends











print(" Welcome to this unstoppable summing software !!! \n")
print("\n")


while True:

    print("Please type below the first number you want to sum : \n")
    print("\n")

    l=[]

    n=input("Type here the number : ")

    while n.isdigit() is False :
        print("\n")
        print(" Sorry, you have to type a number ('integer' of 'float'), no other character is accepted. Please try again. \n")
        n = input("Type here the number : ")


    l.append(n)



    while True:

        q = input("Do you want to sum another number ? (y/n) ")

        while q != "y" and q != "n" and q != "Y" and q != "N":
            print("\n")
            print(" Sorry, you have to type 'y' or 'Y' for summing another number otherwise 'n' or 'N' for stopping this software : ")
            q = input("Do you want to sum another number ? (y/n) ")

        if q == "y" or q == "Y" :
            n = input("Type here the number : ")
            l.append(n)
        elif q == "n" or q =="N" :
            break



    sommatrice(l)


    p = input("Do you want to use this software again ? (y/n) ")


    while p != "y" and p != "n" and p != "Y" and p != "N":
        print("\n")
        print(" Sorry, you have to type 'y' or 'Y' for summing another number otherwise 'n' or 'N' for stopping this software : ")
        p = input("Do you want to continue using this software ? (y/n) ")

    if p == "y" or p == "Y":
        continue
    elif p == "n" or p == "N":
        print("\n")
        print("Thanks for using this software, bye bye ")
        break
