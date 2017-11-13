import random
def main():
    print("\nWelcome to the Guessing Game! This is a 2 player game with 3 rounds. The one with the least guesses wins!")
    play = 'yes' or 'Yes' or 'y' or 'Y'

    while play:
        print("\n(1)easy 1-10  (2)medium 1-50  (3)hard 1-100")
        level = int(raw_input("Choose a level to play: "))
        if level==1:
            max = 10
        elif level == 2:
            max = 50
        else:
            max = 100
        p1score = 0
        p2score = 0


#ROUND 1
        ezgenerate = random.randrange(1, max + 1)
            #print(ezgenerate) #DELETE THIS LATERRRRRRRR

        input1 = int(raw_input("ROUND 1 : For Player 1, choose a number between 1-" + str(max) + ":"))

        while(True):

            if(ezgenerate == input1):
                p1score = p1score + 1
                print"\nCongratulations! You guessed the right number! Player 1's score is:", p1score
                break;

            elif input1 < ezgenerate:
                p1score = p1score + 1
                print("The number you entered is too low.")
                input1 = int(raw_input("Try again: "))

            else:
                p1score = p1score + 1
                print("The number you entered is too high.")

                input1 = int(raw_input("Try again: "))

        ezgenerate2 = random.randrange(1, 11)
            #print(ezgenerate2)  # DELETE THIS LATERRRRRRRR

        input2 = int(raw_input("For Player 2, choose a number between 1-" + str(max) + ":"))

        while (True):

            if (ezgenerate2 == input2):
                p2score = p2score + 1
                print"\nCongratulations! You guessed the right number! Player 2's score is:", p2score
                break;

            elif input2 < ezgenerate2:
                p2score = p2score + 1
                print("The number you entered is too low.")
                input2 = int(raw_input("Try again: "))

            else:
                p2score = p2score + 1
                print("The number you entered is too high.")
                input2 = int(raw_input("Try again: "))
#ROUND 2
        ezgenerate3 = random.randrange(1, 11)
            #print(ezgenerate3)  # DELETE THIS LATERRRRRRRR
        input1 = int(raw_input("ROUND 2 : For Player 1, choose a number between 1-" + str(max) + ":"))

        while(True):

            if(ezgenerate3 == input1):
                p1score = p1score + 1
                print"\nCongratulations! You guessed the right number! Player 1's score is:", p1score
                break;

            elif input1 < ezgenerate3:
                p1score = p1score + 1
                print("The number you entered is too low.")
                input1 = int(raw_input("Try again: "))

            else:
                p1score = p1score + 1
                print("The number you entered is too high.")

                input1 = int(raw_input("Try again: "))

        ezgenerate4 = random.randrange(1, 11)
            #print(ezgenerate4)  # DELETE THIS LATERRRRRRRR

        input2 = int(raw_input("For Player 2, choose a number between 1-" + str(max) + ":"))

        while (True):

            if (ezgenerate4 == input2):
                p2score = p2score + 1
                print"\nCongratulations! You guessed the right number! Player 2's score is:", p2score
                break;

            elif input2 < ezgenerate4:
                p2score = p2score + 1
                print("The number you entered is too low.")
                input2 = int(raw_input("Try again: "))

            else:
                p2score = p2score + 1
                print("The number you entered is too high.")
                input2 = int(raw_input("Try again: "))




#ROUND 3


        ezgenerate5 = random.randrange(1, 11)
            #print(ezgenerate5)  # DELETE THIS LATERRRRRRRR

        input1 = int(raw_input("ROUND 3 : For Player 1, choose a number between 1-" + str(max) + ":"))

        while(True):

            if(ezgenerate5 == input1):
                p1score = p1score + 1
                print"\nCongratulations! You guessed the right number! Player 1's score is:", p1score
                break;

            elif input1 < ezgenerate5:
                p1score = p1score + 1
                print("The number you entered is too low.")
                input1 = int(raw_input("Try again: "))

            else:
                p1score = p1score + 1
                print("The number you entered is too high.")

                input1 = int(raw_input("Try again: "))

        ezgenerate6 = random.randrange(1, 11)
            #print(ezgenerate6)  # DELETE THIS LATERRRRRRRR

        input2 = int(raw_input("For Player 2, choose a number between 1-" + str(max) + ":"))

        while (True):

            if (ezgenerate6 == input2):
                p2score = p2score + 1
                print"\nCongratulations! You guessed the right number! Player 2's score is:", p2score
                break;

            elif input2 < ezgenerate6:
                p2score = p2score + 1
                print("The number you entered is too low.")
                input2 = int(raw_input("Try again: "))

            else:
                p2score = p2score + 1
                print("The number you entered is too high.")
                input2 = int(raw_input("Try again: "))


        if (p1score == p2score):
            print("The game is a tie!")
        elif (p1score < p2score):
            print "\n\nThe winner of the guessing game is Player 1 with a score of:" , p1score
        else:
            print "\n\nThe winner of the guessing game is Player 2 with a score of: ", p2score



        answer = raw_input('\n Play again?  yes/no: ')
        if answer == 'no' or answer == 'N' or answer == 'n' or answer == 'No':
            play = False


main()