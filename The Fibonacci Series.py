

''' In the Fibonacci series, each number in the series is the sum

of the two numbers in the series preceding it,

for example: 1, 1, 2, 3, 5, 8, 13 ...

This is a recursive function that returns in

output the numbers of the Fibonacci sequence,

within a specific threshold set by the user.  '''




# FUNCTION 'calcola_serie_Fibonacci' stars

def calcola_serie_Fibonacci(numero_ingresso) :

    numero=int(numero_ingresso)

    serie_di_Fibonacci=" "

    for i in range(0,numero+1,1) :
        nuovo_elemento=calcola_elemento_serie_Fibonacci(i)
        serie_di_Fibonacci+=str(nuovo_elemento)+" "

    return serie_di_Fibonacci

# FUNCTION 'calcola_serie_Fibonacci' ends






# FUNCTION 'calcola_elemento_serie_Fibonacci' starts

def calcola_elemento_serie_Fibonacci(numero_elemento) :

    numero=int(numero_elemento)

    if numero == 0 :
        elemento_serie_di_Fibonacci=1
        return elemento_serie_di_Fibonacci
    elif numero == 1 :
        elemento_serie_di_Fibonacci=1
        return elemento_serie_di_Fibonacci
    elif numero >= 2 :
        elemento_serie_di_Fibonacci=calcola_elemento_serie_Fibonacci(numero-1)+calcola_elemento_serie_Fibonacci(numero-2)
        return elemento_serie_di_Fibonacci

# FUNCTION 'calcola_elemento_serie_Fibonacci' ends




print("\n")
print("Welcome to this simple software to return the Fibonacci's series \n")
print("\n")

while True:

    print("\n")
    input_number=input(f"Type here the number you want the Fibonacci's series returned : ")

    while input_number.isdigit() == False :
        print("\n")
        print(f"You typed something wrong ! You have to type an integer number ex. 23, 45 \n")
        input_number=input("Type here the number you want the Fibonacci's series returned : \n")

    risultato=calcola_serie_Fibonacci(input_number)
    print("\n")
    print(f"The Fibonacci's series of integer number {input_number} is : {risultato}")
    print("\n")
    scelta=input(f"Do you want to get another Fibonacci's series ? (y/n)")

    while scelta != 'y' and scelta != 'n' :
        print("\n")
        print(f"You typed something wrong ! You have to type 'y' if you want to use this software again ot 'n' to exit ! \n")
        scelta = input(f"Do you want to get another Fibonacci's series ? (y/n)")
        print("\n")

    if scelta == 'y ' :
        continue
    elif scelta == 'n' :
        print("\n")
        print(f"Thanks for using this software ! Bye bye. ")
        print("\n")
        break

 

 

 

 

 
