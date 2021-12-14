def card(number):
    number = number.split()
    number[0], number[1], number[2] = "****", "****", "****"
    print(" ".join(number))

card(input("enter card number"))