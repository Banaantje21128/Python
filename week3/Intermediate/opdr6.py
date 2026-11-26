vraag = input(f"Ben u lid? Type ja als het zo is, en als het niet zo is zeg dan nee: ")
prijs = float(24.99)

som = prijs * 0.90

if vraag == "ja":
    print(f"Dit is de prijs: {som}")
elif vraag == "nee":
    print(f"Dit is de prijs: {prijs}")