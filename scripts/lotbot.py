import random as rand

"""
This is the lottery bot class that will guess powerball numbers
an perform various other data analysis as updated.
@Author: Nolan Jordan
"""

class lotbot:
# constructor #
	def __init__(self):
		self.sample = []
		self.value = [0,0,0,0,0,0]

# class methods #

	def randomGuess(self):
		temp = self.value
		for x in range(len(temp)):
			if x != 5:
				temp[x] = rand.randint(1,69)
			else:
				temp[x] = rand.randint(1, 26)
				break
		self.value = temp

	def show(self):
		print(self.value)

    
        
