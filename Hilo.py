import random
"""
Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.


"""
class HiloGame: # class name
    def __init__(self):#function for intializing the game
         self.score =300 #player starts with ponts
         self.is_playing = True
         self.card = random.randint(1,13)
         self.card_list =[1,2,3,4,5,6,7,8,9,10,11,12,13]
         self.card_list_len=len(self.card_list)
    
    def start_game(self):
        while (self.score > 0):
            self.print_card()
            self.guess()
            self.print_score()
        print("game over!")
        print("Your score is: ", self.score)

    def print_card(self):
        print("current card: ", self.card) 

    def guess(self):
        guess = input("choose ( Higher / Lower)")




        
        