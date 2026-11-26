jaartal = int(input("Jaartal: "))

if jaartal % 4 == 0 and jaartal % 100 != 0 or jaartal % 400 == 0:
    print(f"{jaartal} is een schrikkeljaar")
else:
    print(f"{jaartal} is geen schrikkeljaar")