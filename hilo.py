# Create a dice game.
# The player starts with 300 points.
# Individual cards are represented by numbers 1-13.
# The current card is displayed on the screen.
# The player guesses if the next one will be higher or lower.
# The next card is displayed 
# The player earns 100 points for each correct guess.
# The player loses 75 points for each incorrect guess.
# The game ends when the player runs out of points.
# The player can choose to quit at any time.
# The game should display the total score at the end.

import random

class DiceGame:
    """
    The player starts with 300 points.
    Individual cards are represented by numbers 1-13.
    The current card is displayed on the screen.
    The player guesses if the next one will be higher or lower.
    The next card is displayed 
    The player earns 100 points for each correct guess.
    The player loses 75 points for each incorrect guess.
    The game ends when the player runs out of points.
    The player can choose to quit at any time.
    The game should display the total score at the end.
    """
    def __init__(self):
        # initialize the game
        self.score = 300 # player starts with 300 points
        self.is_playing = True # player is playing
        self.card = random.randint(1, 13) # current card
        self.card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.card_list_len = len(self.card_list)

class Hilogame(DiceGame):
    """
    The player starts with 300 points.
    Individual cards are represented by numbers 1-13.
    The current card is displayed on the screen.
    The player guesses if the next one will be higher or lower.
    The next card is displayed 
    The player earns 100 points for each correct guess.
    The player loses 75 points for each incorrect guess.
    The game ends when the player runs out of points.
    The player can choose to quit at any time.
    The game should display the total score at the end.
    """
    def __init__(self):
        # initialize the game
        self.score = 300 # player starts with 300 points
        self.is_playing = True # player is playing
        self.card = random.randint(1, 13) # current card
        self.card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.card_list_len = len(self.card_list)

    def play(self):
        # play the game
        while self.is_playing:
            self.card = random.randint(1, 13) # current card
            self.card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            self.card_list_len = len(self.card_list)
            self.guess()
            self.score -= 75 # lose 75 points for each incorrect guess
            if self.score <= 0:
                self.is_playing = False
                print("You ran out of points. You lost.")
                print("Your score:", self.score)
                break
            else:
                print("Your score:", self.score)
                print("Do you want to play again? (y/n)")
                answer = input()
                if answer == "y":
                    self.is_playing = True
                else:
                    self.is_playing = False
                    print("Your score:", self.score,"\nThanks for playing! Game over.")
                    break

    def guess(self):
        # guess if the next card will be higher or lower
        print("The current card is:", self.card)
        print("Will the next card be higher or lower?")
        answer = input()
        if answer == "higher":
            self.card_list.remove(self.card)
            self.card_list_len = len(self.card_list)
            self.card = random.choice(self.card_list)
            print("The next card is:", self.card)
            self.score += 100
        elif answer == "lower":
            self.card_list.remove(self.card)
            self.card_list_len = len(self.card_list)
            self.card = random.choice(self.card_list)
            print("The next card is:", self.card)
            self.score -= 75
        else:
            print("Invalid answer.")
            self.guess()


if __name__ == '__main__':
   game = Hilogame()
   game.play()