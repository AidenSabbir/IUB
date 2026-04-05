used = int(input("Enter the number of units used: "))
if used <= 100:
    used = used*0.50
elif used <= 200:
    used = used*0.75
print(f"The electricity bill is: {used}")
