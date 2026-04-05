age = int(input("Enter your age: "))
student = input("Are you a student yes/no: ")
fare = 2.50
if age >=18:
    if age >= 65:
        fare -= fare*(40/100)
    if student == "yes":
        fare -= fare*(25/100)
else:
    fare = 0
print(f"The fare is: {fare}")