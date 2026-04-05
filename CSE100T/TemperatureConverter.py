t = input("Enter Temp in Format 30F, 200K, 72F").lower()
num = float(t[:-1])
if t[-1] == 'c':
    print(f'Temp in C: {num:.2f}C\nTemp in K:{(273+num):.2f}K\nTemp in F:{((num*9/5)+32):.2f}F')
elif t[-1] == 'k':
    print(f'Temp in C: {(num-273):.2f}C\nTemp in K:{num:.2f}K\nTemp in F:{(((num-273)*9/5)+32):.2f}F')
elif t[-1] == 'f':
    print(f'Temp in C: {((num-32)/1.8):.2f}C\nTemp in K:{(((num-32)/1.8)+273):.2f}K\nTemp in F:{num:.2f}F')
