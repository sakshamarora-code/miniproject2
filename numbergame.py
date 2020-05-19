"""
# Interactive Guess the Number Game

"""
"""""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number
    Compare the guess number with the secret number
    If the player guesses the right number he wins,
    so print player wins and computer lose.
    If the player guesses the wrong number,
    then he loses so print player lose and computer wins.

"""
"""
Challenge 2
    Print the secret number and guess number when Player loses using format function
"""
"""
Challenge 3
    Print too HIGH or too LOW messages for bad guesses using elif.
"""
"""
Challenge 4
    Let people play again and again until he guesses the right secret number
"""
"""
Challenge 5
Limit the number of guesses to maximum 6 tries
"""
"""
Challenge 6
    Print the number of tries left
"""
"""
Challenge 7
    Lets give user the option to play again
""
Challenge 8
    Catch when someone submits a non integer
"""
print("-----WELCOME TO NUMBER GAME BY SAKSHAM ARORA-DAVIET,JALANDHAR----")
import random 
secret_number = random.randint(1,10)
guesses = 0 
max_tries = 6
while (guesses < max_tries):
    try:
        guess_number = int(input(" Guess a number between 1 and 10 > ") )
        if ( guess_number == secret_number ) :
            print ( " Player Wins and Computer Loses " )  
            break
    except:
        print("Sorry you entered non integer")
    else :
        guesses+=1
        print ( " Player Loses and Computer Wins " )
        print ( " Player has {} tries left ".format(max_tries - guesses) ) 
        if (guess_number < secret_number ) :
            print ( " Player guessed LOW" ) 
        elif (guess_number > secret_number ) : 
            print ( " Player guessed HIGH" ) 
        ans = input("Do you want to play again(Y/N):-")
        if (ans == 'n' or ans == 'N'):
           break
