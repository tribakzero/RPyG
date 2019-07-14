inventory = {
  'arrows': 10,
  'hearts': 3
}

def showItems():
  print("Inventory:")
  for item in inventory:
    print(item + ": " + str(inventory[item]))
  print()

def addItems(items):
  for item in items:
    if item not in inventory:
      inventory[item] = 1
  showItems()

