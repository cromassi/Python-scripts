''' Palindrome sentences.

     This is a function to which a word e is passed

     recognizes if it is a palindrome (words that yes

     they read the same also in reverse) or less '''







# FUNCTION 'inverti_stringa' starts

def inverti_stringa(string) :
    l=len(string)
    inv_string=""


    for i in range(l-1, 0, -1) :
        inv_string += string[i]

    inv_string += string[0]
    return inv_string

# FUNCTION 'inverti_stringa' ends

 
