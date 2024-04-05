import random
items = ['Sten', 'Sax', 'Påse']
dator = ""

# Spelare väljer sten, sax eller påse.
def spel(spelare):
    return spelare
spelare_item = spel("Sax")

# Dator slumpar värde från items.
dator = random.choice(items)

# Spelet loopar tills spelaren vinner datorn.
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


