''' This is a password-generating function.

The function must generate an alphanumeric string of 8 characters

if the user wants a simple password, or

of 20 ascii characters if you want a more complicated password. '''






# FUNCTION 'genera_password' stars

def genera_password(tipo_di_password) :

    import random
    import string

    if tipo_di_password == 's' :
        print("\n")
        print(f"You selected a simple password (string of eight alphanumerical characters) \n")
        print("\n")
        lettere= string.ascii_letters
        caratteri=string.digits
        caratteri+=lettere
        password_semplice=" "

        for i in range(0, 8, 1) :
            password_semplice += random.choice(caratteri)

        """ password=[random.choice(caratteri) for i in range(0,8,1)]
                    password_semplice=str(password) 

                    NOTE: This code works but it generates a list not a string as simple password """

        return password_semplice

    elif tipo_di_password == "c" :
        stringa_ASCII="$&*_@#~"
        stringa_ASCII+=string.ascii_letters

        """
        Alternatively to the previous line:
        
        stringa_ASCII+=string.lowercase
        stringa_ASCII+=string.uppercase
        
        """
        stringa_ASCII+=string.digits
        password_complessa=" "

        for i in range(0, 20, 1) :
            password_complessa += random.choice(stringa_ASCII)

        return password_complessa

# FUNCTION 'genera_password' ends









print("\n")
print("Welcome to this simple software to generare a simple or complex passwprd \n")
print("\n")

while True :

    p = input(f"Do you need a simple (string of eight alphanumerical characters) or complex (string of 20 ASCII characters) password ? (s/c) : \n")

    while p != "s" and p != "c" :
        print("\n")
        print(f"Sorry, you have to type 's' for a simple password otherwise 'c' for a complex password : ")
        p=input(f"What kind of password you need ? (s/c) : ")

    password_finale=genera_password(p)
    print("\n")
    print(f"Your new password is {password_finale}")
    print("\n")
    s=input(f"Do you need another password ? (y/n) : ")

    while  s != 'y' and s != 'n' :
        print("\n")
        s = input(f"Sorry, you typed something wrong ! "
                  f"You have to type ' y' if you need another password or 'n' to exit : ")

    if s == 'y' :
        print("\n")
        continue
    elif s == 'n' :
        print("\n")
        print("Thanks for using this software, bye bye ")
        print("\n")
        break

 

 

 

 

 

"""

Esercizio 017: Funzione Fattoriale Ricorsiva.

Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.


"""

# FUNCTION 'calcola_fattoriale' stars

def calcola_fattoriale(numero_ingresso) :

    numero=int(numero_ingresso)

    if numero == 0 or numero == 1 :
        return numero

    elif numero >= 2 :
        fattoriale=numero*calcola_fattoriale(numero-1)
        return fattoriale

# FUNCTION 'calcola_fattoriale' ends





print("\n")
print("Welcome to this simple software to calculate the factorial of an integer number \n")
print("\n")

while True:

    print("\n")
    input_number=input(f"Type here the number you want the factorial calculated : ")

    while input_number.isdigit() == False :
        print("\n")
        print(f"You typed something wrong ! You have to type an integer number ex. 23, 45 \n")
        input_number=input("Type here the number you want the factorial calculated : \n")

    risultato=calcola_fattoriale(input_number)
    print("\n")
    print(f"The factorial of {input_number} is {risultato}")
    print("\n")
    scelta=input(f"Do you want to calculate another factorial ? (y/n)")

    while scelta != 'y' and scelta != 'n' :
        print("\n")
        print(f"You typed something wrong ! You have to type 'y' if you want to use this software again ot 'n' to exit ! \n")
        scelta = input(f"Do you want to calculate another factorial ? (y/n)")
        print("\n")

    if scelta == 'y ' :
        continue
    elif scelta == 'n' :
        print("\n")
        print(f"Thanks for using this software ! Bye bye. ")
        print("\n")
        break

 

 

 

 

 

 
