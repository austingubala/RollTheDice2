#Austin Gubala
#Copyright 2022

#Importing time
import time

#Importing random integers and giving Dice Roll values
from random import randint as DiceRoll

#Defining methods
def RollTwoDice():
    return (DiceRoll (1,6), DiceRoll (1,6))

#Get the player's name
def GetPlayerName():
    PlayerName = None
    while not PlayerName: #Loop, while nothing is entered
        PlayerName = input('Please enter your name')
    return PlayerName

#Get the player's guess number
def GetPlayersGuessNumber():
    GuessNumber = None
    while GuessNumber is None: #Loop, while nothing is entered
        try:
            GuessNumber = int (input('Please enter a number.'))
        except ValueError:
            print('You did not a number. Please enter a WHOLE number.')
    return GuessNumber

#Win the game, lose the game definitions
def WinGame():
    print('You win the game!')

def LoseGame():
    print ('Yikes, looks like you lost the game!')

#Defining the gameplay loop
def Game():
    CurrentDice = RollTwoDice()
    PlayerName = GetPlayerName()
    MaxGuesses = 5

    #A loop for a maximum of five guesses
    CurrentGuess = 0
    while True:
        GuessNumber = GetPlayersGuessNumber()

        if GuessNumber == sum(CurrentDice):
            WinGame()
            break
        elif CurrentGuess >= MaxGuesses:
            print(f'You should have guessed {sum(CurrentDice)}.')
            LoseGame()
            break
        else:
            
            CurrentGuess += 1
            print('Incorrect.')
            print(f'You have only {MaxGuesses - CurrentGuess} left. ')

    UserWantsToPlayAgain = AskWantToPlayAgain()
    if UserWantsToPlayAgain:
        Game()
    
#Ask the player if they want to play again
def AskWantToPlayAgain():
    WantToPlayAgain = None
    while WantToPlayAgain is None: #Loop, to ask if the player wants to play again
        try:
            WantToPlayAgain = YesOrNo (input('Want to play again?'))
        except ValueError:
            print('Please enter yes or no.')
    return WantToPlayAgain

def YesOrNo(Text: str):
    if Text == 'yes':
        return True
    elif Text == 'no':
        return False
    else:
        raise ValueError
Game()

time.sleep(5)