""" Write a function to which a character is passed as a parameter,
    and which tells us whether the character is a vowel '''




# FUNCTION starts

def scopri_vocale(input_char) :

    vocals_string = ["a", "e", "i", "o", "u"]

    if input_char.isalpha() == True and input_char in vocals_string :
        print(" Great job !!! You typed a vocal character !!! ")
        print("\n")
    else:
        print("\n")
        print(" Not good !!! You didn't type a vocal character !!! ")
        print("\n")

# FUNCTION ends





print("\n")
print(" Hello. welcome to this small software for recognizing a vocal character.")
print("\n")




while True :
    a = input(" Please, type a single character  : ")
    print("\n")


    while len(a) > 1 :
        print("Sorry, you typed a string.....try again \n")
        print("\n")
        a = input(" Please, type a single character  : ")


    scopri_vocale(a)

    print("\n")
    select =input(" Do you want to try again ? : (y/n)")

    while select != "y" and select != "n" :
        print("\n")
        select = input(" Please, type ' y ' if you want to try again otherwise, if you want to stop, type ' n'. Do you want to try again ? : (y/n)")

    if select == "y" :
        continue
    elif select == "n" :
        print("\n")
        print("Ok, thanks for using this software, bye bye !!! ")
        break

 
