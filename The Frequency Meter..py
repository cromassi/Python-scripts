''' This is  a function to which to pass a string as a parameter, and which returns

a dictionary representing the frequency of each character composing the string.

For example, given a string "ababcc", we will get in the result {"a": 2, "b": 2, "c": 2} '''




# FUNCTION 'dizionario_frequenza_caratteri_stringa' starts

def dizionario_frequenza_caratteri_stringa(stringa_ingresso) :

    l=len(stringa_ingresso)
    dizionario_frequenza={ }

    for i in range(0,l,1) :
        dizionario_frequenza[stringa_ingresso[i]] = 0

        for j in range(0,l,1) :

            if stringa_ingresso[i] != stringa_ingresso[j] :
                pass
            elif stringa_ingresso[i] == stringa_ingresso[j] :
                dizionario_frequenza[stringa_ingresso[i]] += 1

    return dizionario_frequenza

# FUNCTION 'dizionario_frequenza_caratteri_stringa' ends








print("\n")
print("Welcome to this simple software to type a text string and get a dictionary of used characters's frequancy. \n")
print("\n")
input_string=input(" Type here a text string : ")
print("\n")
print(f"The string you inserted is '{input_string}' ")
print("\n")
dizionario=dizionario_frequenza_caratteri_stringa(input_string)
print(f"The dictionary of used characters's frequancy is {dizionario}")

 

 
