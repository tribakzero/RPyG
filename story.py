# This program has storytelling and triggers
from items import addItems, showItems

def createDialog(message, actions=None):
	print(message)
	if(actions):
		for action in actions:
			print("「" + str(action) + "」", end=" ")
		selection = input("\nWhat will you do? ")
		triggerStory(actions[selection])

def triggerStory(seed):
	print()
	if seed == "dragon":
		createDialog("There\'s a dragon around, what you want to do?", { "fight": "loot", "run": "run" })
		decision = input()
	if seed == "loot":
		createDialog("You killed the dragon, then picked the loot.")
		addItems(["compass"])
	if seed == "run":
		createDialog("You ran")
