question = str(input("Do you have your ID?(yes or no): "))
print(f"What is your age?: ")
age = int(input())
print(age)

if question == "yes" and age >= 18:
    print("You are an adult so you can buy age bound products.")
elif age < 18:
    print("You can't but products that are age bound because your still underage.")
if question == "no":
    print("You can't buy products that are age bound, since we cant verify your age.")