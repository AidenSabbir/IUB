number = int(input("Enter the number of tickets: "))
total = 0
for i in range(number):
    age = int(input("Enter the age: ")) 
    if age < 1:
        raise ValueError("Invalid age")
    if age < 13:
        total += 8
    elif 13 <= age <=64:
        total += 12  
    elif age > 64:
        total += 10  
    else:
        total += 10
if number > 5:
    total -= total*(15/100)
print(f"The total is: {total}")