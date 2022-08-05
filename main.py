import string
from random import choice

win = 'y'
while win == 'y' or 'Y':

    chars = string.digits
    random = ''.join(choice(chars) for _ in range(4))
    print("random number:", random)
    num_length = len(random)
    number = int(random)
    replay = 'y'
    while replay == 'y':
        rabbit = 0
        tortoise = 0
        # getting input number from user
        user = input("Enter a  four digit number")
        # convert number into string
        randoms = str(random)
        users = str(user)
        # calculating the length of the string
        random_len = len(randoms)
        user_len = len(users)

        # checking the string is integer or not
        user_check = user.isdigit()

        if not user_check:
            print("invalid input")

        elif random_len != user_len:
            print("invalid number")

        elif randoms == users:
            print("WINNER...!")
            win = input("do you want to continue? y/n ")
            while win.lower() not in ("y", "n"):
                win = input("do you want to continue? y/n ")

            if win == "n":
                exit()
        else:
            for i in range(4):
                if randoms[i] == users[i]:
                    rabbit = rabbit + 1

                elif randoms[i] in users:
                    tortoise += 1

            if tortoise > 0:
                print("the number of tortoise are:", tortoise)
            if rabbit > 0:
                print("the number of rabbits are :", rabbit)
        replay = input("do you want to continue? y/n ")

        while replay.lower() not in ("y", "n"):
            replay = input("do you want to continue? y/n ")

        if replay == "n":
            exit()
