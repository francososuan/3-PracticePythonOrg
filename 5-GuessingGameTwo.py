num_password = int(input("Please enter number between 0 and 100: "))
counter = 0
floor = 0
ceiling = 100
guess = 50

while True:
    print("Guess {}: {}" .format(counter+1,guess))
    counter = counter +1

    if guess == num_password:
        print("Congratulations! The password is {}".format(num_password))
        print("The number of tries the computer did was {}".format(counter))
        break

    elif guess > num_password:
        print("Too High!")
        ceiling = guess
        guess = (floor+ceiling)//2

    else:
        print("Too Low!")
        floor = guess
        guess = (floor+ceiling) //2