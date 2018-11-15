"programa para adivinar un numero"

number_to_guess = 2

user_number = int(input("dime un numero"))

if number_to_guess == user_number:
    print("gano")
else:
    print("perido")
    user_number = int(input("dime un numero"))

    if number_to_guess == user_number:
        print("gano")
    else:
        print("perdio")
        user_number = int(input("dime un numero"))

        if number_to_guess == user_number:
            print("gano")
        else:
            print("perdio")
            user_number = int(input("dime un numero"))

            if number_to_guess == user_number:
                print("gano")
            else:
                print("perdio")
                user_number = int(input("dime un numero"))

                if number_to_guess == user_number:
                    print("gano")
                else:
                    print("perdio")
                    print("game over")







