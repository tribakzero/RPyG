# This program has storytelling and triggers
from items import addItems

def createDialog(message, option1=None, option2=None):
	print(message + "\n" + str(option1) + "\n" + str(option2))

def triggerStory(seed):
	if seed == "dragon":
		createDialog("There\'s a dragon around, what you want to do?", "fight", "run")
		decision = input()
	if seed == "loot":
		createDialog("You picked the loot")
		addItems(["compass"])

