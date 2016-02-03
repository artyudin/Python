# Roulette Wheel
# ===============

# a terminal game of Roulette!
# This is a program that takes the player's bet. 
# The player is able to bet on any number of spaces, 
# as well as red, black, odd, even.
# When the user decides to roll, they get the random 
# result and their payout if any. 

import random

class RouletteBet:
	def __init__(self, bet, amount):
		self.bet = bet
		self.amount = amount
		self.ev_od = None
		self.payout = None
		self.number = None
		
	def determine_bet(self):
		self.roll()
		if self.bet == "Red":
			self.payout = 2
			message = self.bet_color()
		elif self.bet == "Black":
			self.payout = 2
			message = self.bet_color()
		elif self.bet == "Odd":
			self.payout = 2
			message = self.even_odd()
		elif self.bet == "Even":
			self.payout = 2
			message = self.even_odd()
		elif self.bet.isdigit() and int(self.bet) in range(1,35):
			self.payout = 35
			message = self.straight_up()
		else:
			message = "This is not a valid bet"
		self.message(message)

	def roll(self):
		self.number = random.randint(1,35)

	

	def bet_color(self):
		red = "Red" if self.number in [1, 3, 5, 7, 9, 12,14, 16,
		18, 19, 21, 23,25, 27, 30, 32, 34, 36] else False
		black = "Black" if self.number in [2, 4, 6, 8, 10, 11,13,
		15, 17, 20, 22, 24,26, 28, 29, 31, 33, 35] else False
		if self.bet == red:
			payout = int(self.amount)*self.payout
			return 'You win:', payout
		elif self.bet == black:
			payout = int(self.amount)*self.payout
			return 'You win:', payout
		else:
			return 'Try Again'


	def even_odd(self):
		even = "Even" if self.number%2 == 0 else False
		odd = "Odd" if self.number%2 != 0 else False

		if self.bet == even:
			payout = int(self.amount)*self.payout
			return 'You win:', payout
		elif self.bet == odd:
			payout = int(self.amount)*self.payout
			return 'You win:', payout
		else:
			return 'Try Again'




	def straight_up(self):
		
		if int(self.bet) == self.number:
			payout = int(self.amount)*self.payout
			return 'You win:', payout
		else:
			return 'Try again'



	def message(self, text):
		print(text)





bt = RouletteBet('Red','1')
bt.determine_bet()