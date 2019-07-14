''' Swedish rövarspråket language.

In Sweden, children often play using a
language a little bit special, called "rövarspråket", which means "
the language of rogues ": consists in doubling
each consonant of a word and insert an "o" in the middle.
For example, the word "eat" becomes "momanongogiarore".
Write a function that can translate a word or
sentence passed through input () in "rövarspråket". '''








# FUNCTION 'leggi_stringa_di_testo' starts

def leggi_stringa_di_testo( ) :

    print("\n")
    input_string = input("Please, type here the string : \n")
    print("\n")

    global len_stringa_ingresso
    len_stringa_ingresso = len(input_string)

    return input_string

# FUNCTION 'leggi_stringa_di_testo' ends







# FUNCTION 'converti_stringa_in_rövarspråket' starts

def converti_stringa_in_rövarspråket(stringa_in_input) :

    print("\n")
    stringa_vocali = "aeiou"
    stringa_caratteri_speciali = "!.,:;     <>?$#@'~|()*+-\/&^%[]{}`"
    stringa_finale=" "

    for i in range(0,len(stringa_in_input),1) :

        if stringa_in_input[i] in stringa_vocali or stringa_in_input[i] in stringa_caratteri_speciali :

            stringa_finale += stringa_in_input[i]

        elif stringa_in_input[i] not in stringa_vocali and stringa_in_input[i] not in stringa_vocali :

            stringa_finale += stringa_in_input[i] + "o" + stringa_in_input[i]

    return stringa_finale

# FUNCTION 'converti_stringa_in_rövarspråket' ends








# FUNCTION 'individua_consonante_in_una_stringa_di_testo' starts

def individua_consonante_in_una_stringa_di_testo(input_string):
    stringa_vocali = "aeiou"
    stringa_caratteri_speciali="!.,:;<>?$#@'~|()*+-\/&^%[]{}`"
    diz_consonanti={}

    for i in range(0,len(input_string),1) :

            if input_string[i] not in stringa_vocali :
                print("\n")
                print(f"Letter {input_string[i]}, which index is {i}, is a consonant !")
                print("\n")
                diz_consonanti[i] = input_string[i]
            elif input_string[i] in stringa_confronto :
                pass

    return diz_consonanti

# FUNCTION 'individua_consonante_in_una_stringa_di_testo' ends









print("\n")
print("Welcome to this simple software to translate a text phrase into 'rövarspråket' ")
print("\n")
stringa_in_ingresso=leggi_stringa_di_testo( )
print(f"The string you inserted is {stringa_in_ingresso}")
print("\n")
print(f"The lenght of the string is {len_stringa_ingresso}")
print("\n")
fin=converti_stringa_in_rövarspråket(stringa_in_ingresso)
print(f"Rövarspråket of the typed string is :{fin}")

 

 

 
