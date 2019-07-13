# max_between_2_numbers


def max_between_2_numbers(n1,n2) :

    if n1 > n2 :
        print(f" Il numero piu' grande e' {n1}")
    elif n1 < n2 :
        print(f"I numero piu' grande e' {n2}")
    else :
        print("I due numeri sono identici")







print("\n")
print("Hello, this a short sofware to compare 2 numbers \n")
print("\n")
a=input("Please , type in the first number: \n")
# c=int(a)
# print(c)
print("\n")
b=input("Please, type in second number : \n")
# d=int(b)
# print(d)
print("\n")


while a.isdigit() == False or b.isdigit() == False :
    print("Sorry , you didn't type numerical values....\n")
    a = input("Please , type in the first number: \n")
    # c=int(a)
    print("\n")
    b = input("Please, type in second number : \n")
    # d=int(b)
    print("\n")


max_between_2_numbers(a, b)

 

 
