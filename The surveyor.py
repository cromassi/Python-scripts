
''' This is a function that, at the user's choice,


calculate the area of: - a circle - a square - a rectangle - a triangle '''






# FUNCTION 'controlla_numero_decimale' starts

def controlla_numero_decimale (valore_in_ingresso) :
    l=len(valore_in_ingresso)

    for i in range(0,l,1) :

        if valore_in_ingresso[i] in "1234567890." :
            risposta_True_or_False = True
        else:
            risposta_True_or_False = False

    return risposta_True_or_False

# FUNCTION 'controlla_numero_decimale' ends









# FUNCTION 'calcola_area_figura_geometrica' starts

def calcola_area_figura_geometrica( ) :
    print("\n")
    print("Select below the geometric figure you want to calculate the area \n")
    print("\n")
    input_user = input("a : circle, b : square, c : rectangle, d : triangle \n")
    print("\n")

    while input_user != "a" and input_user != "b" and input_user != "c" and input_user != "d":
        print("\n")
        print("Sorry, you didn't type any character corresponding to a geometric figure !!! \n")
        print("Type for circle : a \n"
              "Type for square : b \n"
              "Type for rectangle : c \n"
              "Type for triangle : d \n")
        input_user = input()

    if input_user == "a":
        figura_geometrica = "circle"
    elif input_user == "b":
        figura_geometrica = "square"
    elif input_user == "c":
        figura_geometrica = "rectangle"
    elif input_user == "d":
        figura_geometrica = "triangle"
    print("\n")
    print(f"The geometric figure you selected is {figura_geometrica} ")
    print("\n")

    if figura_geometrica == "circle" :
        raggio_cerchio=input("Please, type here the lenght (centimeters) of circle's ray you want to calculate the area : \n")

        risposta = controlla_numero_decimale(raggio_cerchio)

        while risposta != True :
            raggio_cerchio = input("Sorry, you made some typo \n"
                                  "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta = controlla_numero_decimale(raggio_cerchio)

        area_cerchio=3.14*(float(raggio_cerchio)**2)
        print("\n")
        print(f"Area of the circle (in square centimeters) : {area_cerchio}")
        print("\n")

    elif figura_geometrica == "square" :
        lato_quadrato = input("Please, type here the lenght (centimeters) of square's side you want to calculate the area : \n")
        len_lato_quadrato=len(lato_quadrato)
        risposta = controlla_numero_decimale(lato_quadrato)

        while risposta != True :
            lato_quadrato = input("Sorry, you made some typo \n"
                                   "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta=controlla_numero_decimale(lato_quadrato)



        area_quadrato = float(lato_quadrato)**2

        print("\n")
        print(f"Area of the square (in square centimeters) : {area_quadrato}")
        print("\n")

    elif figura_geometrica == "rectangle" :
        base_rettangolo = input("Please, type here the lenght (centimeters) of rectangle's base you want to calculate the area : \n")

        risposta = controlla_numero_decimale(base_rettangolo)

        while risposta != True :
            base_rettangolo = input("Sorry, you made some typo \n"
                                    "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta = controlla_numero_decimale(base_rettangolo)


        altezza_rettangolo = input("Please, type here the lenght (centimeters) of rectangle's heigh you want to calculate the area : \n")

        risposta = controlla_numero_decimale(altezza_rettangolo)

        while risposta != True :
            altezza_rettangolo = input("Sorry, you made some typo \n"
                                       "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta = controlla_numero_decimale(altezza_rettangolo)


        area_rettangolo = float(base_rettangolo)**float(altezza_rettangolo)
        print("\n")
        print(f"Area of the rectangle (in square centimeters) : {area_rettangolo}")
        print("\n")

    elif figura_geometrica == "triangle" :
        base_triangolo = input("Please, type here the lenght (centimeters) of triangle's base you want to calculate the area : \n")

        risposta = controlla_numero_decimale(base_triangolo)

        while risposta != True :
            base_triangolo = input("Sorry, you made some typo \n"
                                   "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta = controlla_numero_decimale(base_triangolo)



        altezza_triangolo = input("Please, type here the lenght (centimeters) of triangle's heigh you want to calculate the area : \n")

        risposta = controlla_numero_decimale(altezza_triangolo)

        while risposta != True :
            altezza_triangolo = input("Sorry, you made some typo \n"
                                      "Please, type here the lenght in centimeters (ex. 15 - 23.6 - 78.234) : ")
            risposta = controlla_numero_decimale(altezza_triangolo)

        area_triangolo = (float(base_triangolo)*float(altezza_triangolo))/2
        print("\n")
        print(f"Area of the triangle (in square centimeters) : {area_triangolo}")
        print("\n")

# FUNCTION 'calcola_area_figura_geometrica' ends












print("\n")
print("Welcome to this simple software to calculate the area of a circle/square/rectangle/triangle \n")
print("\n")
calcola_area_figura_geometrica( )
