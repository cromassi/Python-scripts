''' This is a function which, given an input of a list A containing words, returns an output

list B of integers representing the length of the words contained in A'''









# FUNCTION 'converti_lista_di_parole_in_lista_delle_loro_lunghezze' starts

def converti_lista_di_parole_in_lista_delle_loro_lunghezze (list_input) :
    l_input=len(list_input)
    global a
    lenghts=[]

    for i in range(0,l_input,1) :
        lenghts.append(len(list_input[i]))

    a=lenghts
    # return lenghts

# FUNCTION 'converti_lista_di_parole_in_lista_delle_loro_lunghezze' ends










print("\n")
print("Welcome to this simple software to convert a list of words into a list of their lenghts ")
print("\n")

list = []

print("\n")
in_list = input("Please, type here the first element of the list (it has to be a word, just letters) : \n")
print("\n")

while in_list.isalpha() == False :
    print("\n")
    in_list=input(" Sorry, you didn't type a word !!! Please type a word : \n")
    print("\n")

if in_list.isalpha() == True :
    list.append(in_list)
    l= 1


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

        while in_list.isalpha() == False:
            print("\n")
            in_list = input("Sorry, you didn't type a word !!! Please type a word (just letters) : \n")
            print("\n")

        if in_list.isalpha() == True:
            list.append(in_list)
            l += 1
            print("\n")



print("\n")
print(f"The list you inserted is {list}")
print("\n")
print(f"The lenght of the list is {l}")
print("\n")
# a=converti_lista_di_parole_in_lista_delle_loro_lunghezze(list)
converti_lista_di_parole_in_lista_delle_loro_lunghezze(list)
print("\n")
print("The list of all lenghts of all words you typed as elements of the original list is \n")
print("\n")
print(a)
print("\n")
print("Thanks for using this software ! Bye bye \n")
print("\n")

 

 
 

 

 
