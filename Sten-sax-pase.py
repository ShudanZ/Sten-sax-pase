
import random
items = ['Sten', 'Sax', 'Påse']
dator = ""

def spel(spelare):
    return spelare
spelare_item = spel("Sax")

dator = random.choice(items)
if spelare_item == "Sten":
    while dator != "Sax":
        print("dator is", dator, "spelare is", spelare_item, "Try again.")
        dator = random.choice(items)
    print("dator is", dator, "spelare is", spelare_item, "You win!")

if spelare_item == "Sax":
    while dator != "Påse":
        print("dator is", dator, "spelare is", spelare_item, "Try again.")
        dator = random.choice(items)
    print("dator is", dator, "spelare is", spelare_item, "You win!")
    
if spelare_item == "Påse":
    while dator != "Sten":
        print("dator is", dator, "spelare is", spelare_item, "Try again.")
        dator = random.choice(items)
    print("dator is", dator, "spelare is", spelare_item, "You win!")


