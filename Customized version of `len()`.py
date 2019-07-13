''' Customized version of `len()`

    This function sends the length of a string to print or list passed as a parameter. In essence, albeit present, try to write your version of the len () function '''









# FUNCTION 'calcola_lunghezza_stringa' starts

def calcola_lunghezza_stringa(string) :

    lunghezza_stringa = 0

    for i in string :
        lunghezza_stringa += 1

    return lunghezza_stringa

# FUNCTION 'calcola_lunghezza_stringa' ends






print("\n")
print("Welcome to this simple software to calculate the lenght of a string or list ")
print("\n")



while True :

    print("\n")
    q=input("Do you want to get the lenght of a string or a list ? (s/l) : ")
    print("\n")

    while q != "s" and q != "S" and q != "l" and q != "L":
        print("\n")
        print(" Sorry, you have to type 's' or 'S' for the lenght of a string otherwise 'l' or 'L' for  : ")
        p = input("Do you want to get the lenght of a string or a list ? (s/l) :")


    if q == "s" or q == "S" :
        print("\n")
        s=input(" Please type here the original text string : ")
        print("\n")

        l_s=calcola_lunghezza_stringa(s)

        print("The lenght is  : " + str(l_s))
        print("\n")


    elif q == "l" or q == " L " :

        list=[]

        print("\n")
        in_list=input("Please, type here the first element of the list : ")
        print("\n")
        list.append(in_list)
        l_l=1

        while True:

            q = input("Do you want to add another element to the list ? (y/n) : ")

            while q != "y" and q != "n" and q != "Y" and q != "N":
                print("\n")
                print(" Sorry, you have to type 'y' or 'Y' for adding a new element to the list otherwise 'n' or 'N' for closing the list : ")
                q = input("Do you want to add another element to the list ? (y/n) : ")

            if q == "n" or q == "N":
                print("\n")
                print("List finished")
                print("\n")
                break

            elif q == "y" or q == "Y":
                print("\n")
                in_list = input("Please, type here the new element of the list : ")
                list.append(in_list)
                l_l += 1
                print("\n")



        print("\n")
        print(f"The list you inserted is {list}")
        print("\n")
        print(f"The lenght of the list is {l_l}")
        print("\n")




    p = input("Do you want to use this software again ? (y/n) ")

    while p != "y" and p != "n" and p != "Y" and p != "N":
        print("\n")
        print(" Sorry, you have to type 'y' or 'Y' for ci=ontinuining to use this software otherwise 'n' or 'N' for stopping this software : ")
        p = input("Do you want to continue using this software ? (y/n) ")

    if p == "y" or p == "Y":
        continue

    elif p == "n" or p == "N":
        print("\n")
        print("Thanks for using this software, bye bye ")
        break

 

 
