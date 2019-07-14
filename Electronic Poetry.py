
''' This is a simple "rime creator" function, to which a list of words is passed,


and compares it with a search word entered by the user


of rhymes, understood as words whose last 3 letters are equal to the word given!  ''' 









# FUNCTION 'main' starts

def main() :

    # print(__name__)
    print(f"\n")
    print(f"Welcome to this simple software to search for rhymes. \n")
    print(f"\n")
    parola_da_cercare=input(f"Type here the word you want to search a rhyme for (at least three letters) : \n")

    while parola_da_cercare.isalpha() != True or len(parola_da_cercare) < 3 :
        print(f"\n")
        print("Sorry, you typed something wrong ! Never type in numbers or special characters, just at least three letters \n")
        print("\n")
        parola_da_cercare=input(f"Type here the word you want to search a rhyme for : \n")
        print(f"\n")

    elenco_rime_trovate=cerca_rime(parola_da_cercare)
    # risultato=elenco_rime_trovate[0]
    # rhyme=elenco_rime_trovate[1]
    # conteggio=elenco_rime_trovate[2]

    if elenco_rime_trovate[2] == 0 :
        print(f"Sorry, no rhymes of the word '{parola_da_cercare}' were found (the rhyme is `{elenco_rime_trovate[1]}`)\n")
        print("\n")

    elif elenco_rime_trovate[2] == 1 :
        print(f"Found one rhyme of the word '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
              f"\n"
              f"> {elenco_rime_trovate[0]} " )
        print("\n")

    else :
        print(f"Found {elenco_rime_trovate[2]} rhymes of the word '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
              f"\n"
              f"> {elenco_rime_trovate[0]} " )
        print("\n")

    while True:

        print("\n")
        scelta=input(f"Do you want to search for another rhyme ? (y/n)")

        while scelta != 'y' and scelta != 'n' :
            print(f"\n")
            print(f"You typed something wrong ! You have to type 'y' if you want to use this software again (and get new rhyme/rhymes) ot 'n' to exit ! \n")
            scelta = input(f"Do you want to search for another rhyme ? (y/n)")
            print(f"\n")

        if scelta == 'y' :
            print(f"\n")
            parola_da_cercare=input(f"Type here the word you want to search a rhyme for (at least three letters) : \n")

            while parola_da_cercare.isalpha() != True or len(parola_da_cercare) < 3:
                print(f"\n")
                print(f"Sorry, you typed something wrong ! Never type in numbers or special characters, just at least three letters \n")
                print("\n")
                parola_da_cercare = input(f"Type here the word you want to search a rhyme for : \n")
                print(f"\n")

            elenco_rime_trovate=cerca_rime(parola_da_cercare)
            # risultato=elenco_rime_trovate[0]
            # rhyme=elenco_rime_trovate[1]
            # conteggio=elenco_rime_trovate[2]

            if elenco_rime_trovate[2] == 0:
                print(f"Sorry, no rhymes of '{parola_da_cercare}' were found (the rhyme is `{elenco_rime_trovate[1]}`)\n")

            elif elenco_rime_trovate[2] == 1:
                print(f"Found one rhyme of '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
                      f"\n"
                      f"> {elenco_rime_trovate[0]} ")

            else:
                print(f"Found {elenco_rime_trovate[2]} rhymes of '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
                      f"\n"
                      f"> {elenco_rime_trovate[0]} ")

            continue

        elif scelta == 'n' :
            print(f"\n")
            print(f"Thanks for using this software! Bye bye. ")
            print(f"\n")
            break

# FUNCTION 'main' ends


 

"""
Try to import the script `exercise_020.py`

"""



import exercise_020






# FUNCTION 'main' starts

def main() :

    # print(exercise_020.__name__)
    print(f"\n")
    print(f"Welcome to this simple software to search for rhymes. \n")
    print(f"\n")
    parola_da_cercare = input(f"Type here the word you want to search a rhyme for (at least three letters) : \n")

    while parola_da_cercare.isalpha() != True or len(parola_da_cercare) < 3:
        print(f"\n")
        print(
        "Sorry, you typed something wrong ! Never type in numbers or special characters, just at least three letters \n")
        print("\n")
        parola_da_cercare = input(f"Type here the word you want to search a rhyme for : \n")
        print(f"\n")

    elenco_rime_trovate=exercise_020.cerca_rime(parola_da_cercare)
    # risultato=elenco_rime_trovate[0]
    # rhyme=elenco_rime_trovate[1]
    # conteggio=elenco_rime_trovate[2]

    if elenco_rime_trovate[2]== 0:
        print(f"Sorry, no rhymes of the word '{parola_da_cercare}' were found (the rhyme is `{elenco_rime_trovate[1]}`)\n")
        print("\n")

    elif elenco_rime_trovate[2] == 1:
        print(f"Found one rhyme of the word '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
              f"\n"
              f"> {elenco_rime_trovate[0]} ")
        print("\n")

    else:
        print(f"Found {elenco_rime_trovate[2]} rhymes of the word '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
              f"\n"
              f"> {elenco_rime_trovate[0]} ")
        print("\n")

    while True:

        print("\n")
        scelta = input(f"Do you want to search for another rhyme ? (y/n)")

        while scelta != 'y' and scelta != 'n':
            print(f"\n")
            print(f"You typed something wrong ! You have to type 'y' if you want to use this software again (and get new rhyme/rhymes) ot 'n' to exit ! \n")
            scelta = input(f"Do you want to search for another rhyme ? (y/n)")
            print(f"\n")

        if scelta == 'y':
            print(f"\n")
            parola_da_cercare = input(f"Type here the word you want to search a rhyme for (at least three letters) : \n")

            while parola_da_cercare.isalpha() != True or len(parola_da_cercare) < 3:
                print(f"\n")
                print(f"Sorry, you typed something wrong ! Never type in numbers or special characters, just at least three letters \n")
                print("\n")
                parola_da_cercare = input(f"Type here the word you want to search a rhyme for : \n")
                print(f"\n")

            elenco_rime_trovate=exercise_020.cerca_rime(parola_da_cercare)
            # risultato=elenco_rime_trovate[0]
            # rhyme=elenco_rime_trovate[1]
            # conteggio=elenco_rime_trovate[2]

            if elenco_rime_trovate[2] == 0:
                print(f"Sorry, no rhymes of '{parola_da_cercare}' were found (the rhyme is `{elenco_rime_trovate[1]}`)\n")

            elif elenco_rime_trovate[2] == 1:
                print(f"Found one rhyme of '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
                      f"\n"
                      f"> {elenco_rime_trovate[0]} ")

            else:
                print(f"Found {elenco_rime_trovate[2]} rhymes of '{parola_da_cercare}' (the rhyme is `{elenco_rime_trovate[1]}`) :\n"
                      f"\n"
                      f"> {elenco_rime_trovate[0]} ")

            continue

        elif scelta == 'n':
            print(f"\n")
            print(f"Thanks for using this software! Bye bye. ")
            print(f"\n")
            break

# FUNCTION 'main' ends









if __name__ == "__main__" :
    main()

 
 

 
