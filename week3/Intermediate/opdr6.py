vraag = input(f"Ben u lid? Type ja als het zo is, en als het niet zo is zeg dan nee: ")
prijs = float(24.99)

som = prijs * 0.90
afgerond = round(som, 2)

if vraag == "ja":
    print(f"Dit is de prijs: {afgerond} euro.")
elif vraag == "nee":
    print(f"Dit is de prijs: {prijs} euro.")