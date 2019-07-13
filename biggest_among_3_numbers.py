'''Write a function that takes three numbers this time

    as a parameter and returns the largest of them! '''


def max_between_3_numbers(n1,n2,n3) :

    if n1 > n2 and n1 > n3 and n2 > n3 :
        print(f" Il numero piu' grande e' first number {n1}, poi ci sono second number {n2} ed infine third number {n3} ")
    elif n1 > n2 and n1 > n3 and n2 < n3 :
        print(f" Il numero piu' grande e' first number {n1}, poi ci sonothird number {n3} ed infine second number {n2} ")
    elif n1 < n2 and n1 > n3 and n2 > n3:
        print(f" Il numero piu' grande e' second number {n2}, poi ci sono first number {n1} ed infine {n3} ")
    elif n1 < n2 and n1 < n3 and n2 > n3:
        print(f" Il numero piu' grande e' second number{n2}, poi ci sono {n3} ed infine first number {n1} ")
    elif n1 > n2 and n1 < n3 and n2 < n3:
        print(f" Il numero piu' grande e' third number {n3}, poi ci sono first number {n1} ed infine second number {n2} ")
    elif n1 < n2 and n1 < n3 and n2 < n3:
        print(f" Il numero piu' grande e' third number {n3}, poi ci sono second number {n2} ed infine first number {n1} ")
    elif n1 > n2 and n1 > n3 and n2 == n3:
        print(f" Il numero piu' grande e' {n1}, poi ci sono second number {n2} = third number {n3} ")
    elif n1 < n2 and n1 == n3 and n2 > n3:
        print(f" Il numero piu' grande e' second number {n2}, poi ci sono first number {n1} = third number {n3} ")
    elif n1 == n2 and n1 < n3 and n2 < n3:
        print(f" Il numero piu' grande e' third number {n3}, poi ci sono first number {n1} = second number {n2} ")
    elif n1 == n2 and n1 > n3 and n2 > n3:
        print(f" I numeri piu' grandi sono first number {n1} = second number {n2}, poi c'e' third number {n3} ")
    elif n1 > n2 and n1 == n3 and n2 < n3:
        print(f" I numeri piu' grandi sono first number {n1} = third number {n3}, poi c'e'second number  {n2} ")
    elif n1 < n2 and n1 < n3 and n2 == n3:
        print(f" I numeri piu' grandi sono second number {n2} = third number {n3}, poi c'e'first number {n1} ")
    else:
        print(f" I tre numeri sono uguali ")





print("\n")
print("Hello, this a short sofware to compare 3 numbers \n")
print("\n")
a=input("Please , type in the first number: \n")
print("\n")
b=input("Please, type in second number : \n")
print("\n")
c=input("Please, type in third number : \n")
print("\n")

while a.isdigit() == False or b.isdigit() == False or c.isdigit() == False :

    print("Sorry , you didn't type numerical values....\n")
    a = input("Please , type in the first number: \n")
    print("\n")
    b = input("Please, type in second number : \n")
    print("\n")
    c = input("Please, type in third number : \n")
    print("\n")

max_between_3_numbers(int(a),int(b),int(c))
