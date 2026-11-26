getal1 = float(input("Type een getal:"))
getal2 = float(input("Type nog een getal:"))

som = getal1 + getal2
verschil = getal1 - getal2
product = getal1 * getal2

if getal2 != 0:
    quotient = getal1 / getal2
else:
    quotient = "neit mogelijk te delen door 0"

print(f"Resultaat van {getal1} en {getal2}")

print(f"optellen: {som}")

print(f"verschillende getal: {verschil}")

print(f"producti: {product}")

print(f"quotient: {quotient}")