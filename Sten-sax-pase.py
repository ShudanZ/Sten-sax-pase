import random
items = ['Sten', 'Sax', 'Påse']
dator = ""
spelare = ""

# Spelare väljer sten, sax eller påse.
spelare = input("Select from 'Sten', 'Sax' and 'Påse': ")

# Dator slumpar värde från items.
dator = random.choice(items)

# Spelet loopar tills spelaren vinner datorn.
while True:
    if ((spelare == "Sten" and dator == "Sax") or (spelare == "Sax" and dator == "Påse") or (spelare == "Påse" and dator == "Sten")):
        print("dator is", dator, "spelare is", spelare, "You win!")
        break 
    print("dator is", dator, "spelare is", spelare, "Try again.")
    dator = random.choice(items)
    spelare = input("Select from 'Sten', 'Sax' and 'Påse': ")

