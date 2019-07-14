''' This function calculates the factorial of a number '''



 # FUNCTION 'calcola_fattoriale' stars

def calcola_fattoriale() :

    print("\n")
    print("Welcome to this simple software to calculate the factorial of an integer number \n")
    print("\n")

    while True:

        print("\n")
        input_number = input(f"Type here the number you want the factorial calculated : ")

        while input_number.isdigit() == False:
            print("\n")
            print(f"You typed something wrong ! You have to type an integer number ex. 23, 45 \n")
            input_number = input("Type here the number you want the factorial calculated : \n")


        number=int(input_number)





        print("\n")
        print(f"The factorial of {input_number} is {risultato}")
        print("\n")
        scelta = input(f"Do you want to calculate another factorial ? (y/n)")

        while scelta != 'y' and scelta != 'n':
            print("\n")
            print(
                f"You typed something wrong ! You have to type 'y' if you want to use this software again ot 'n' to exit ! \n")
            scelta = input(f"Do you want to calculate another factorial ? (y/n)")
            print("\n")

        if scelta == 'y ':
            continue
        elif scelta == 'n':
            print("\n")
            print(f"Thanks for using this software ! Bye bye. ")
            print("\n")
            break


# FUNCTION 'calcola_fattoriale' ends

calcola_fattoriale()

 

 
