
 


''' A MAC address (media access control address) is an associated unique address

from the manufacturer, to a chipset for wireless communications (eg WiFi or Bluetooth),

composed of 6 alphanumeric pairs of characters.

An example of a MAC is 02: 33: A5: F2: 55: 12.

This function generates_MAC which generates MAC addresses starting from random alphanumeric pairs .  '''








# FUNCTION 'genera_indirizzo _MAC' stars

def genera_indirizzo_MAC() :

    import random
    import string

    print(f"\n")
    stringa_caratteri_per_indirizzo_MAC=string.hexdigits.upper()
    indirizzo_MAC=""

    for i in range(0,5,1) :
        parziale_1=random.choice(stringa_caratteri_per_indirizzo_MAC)
        parziale_2=random.choice(stringa_caratteri_per_indirizzo_MAC)
        indirizzo_MAC+=f"{parziale_1}{parziale_2}:"

    parziale_3=random.choice(stringa_caratteri_per_indirizzo_MAC)
    parziale_4=random.choice(stringa_caratteri_per_indirizzo_MAC)
    indirizzo_MAC += f"{parziale_3}{parziale_4}"

    return indirizzo_MAC

# FUNCTION 'genera_indirizzo _MAC' ends





print(f"\n")
print(f"Welcome to this simple software to generate a MAC Address. \n")
print(f"\n")
risultato=genera_indirizzo_MAC( )
print(f"Your new MAC Addres is  {risultato} " )
print("\n")

while True:

    print("\n")
    scelta=input(f"Do you want to get another MAC Address ? (y/n)")

    while scelta != 'y' and scelta != 'n' :
        print(f"\n")
        print(f"You typed something wrong ! You have to type 'y' if you want to use this software again (and get a new MAC Address) ot 'n' to exit ! \n")
        scelta = input(f"Do you want to get another MAC Address ? (y/n)")
        print(f"\n")

    if scelta == 'y' :
        print(f"\n")
        risultato=genera_indirizzo_MAC()
        print(f"Your new MAC Addres is  {risultato} ")
        print(f"\n")
        continue
    elif scelta == 'n' :
        print(f"\n")
        print(f"Thanks for using this software ! Bye bye. ")
        print(f"\n")
        break

 

 

 

 

 
 

 
