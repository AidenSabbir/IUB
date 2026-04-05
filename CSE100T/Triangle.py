base,hght = map(int,input('Enter Base Height with space (ex. 3 4) >').split())

hyp = (base**2 + hght**2)**0.5

print(f"Area of Tri: {(0.5*base*hght):.2f}\nPerimeter of Tri: {(base+hght+hyp):.2f}\nsinθ: {(hght/hyp):.2f}\ncosθ: {(base/hyp):.2f}\ntanθ: {(base/hght):.2f}")
print('\nGraphical rep: ')
for i in range(1,hght+1):
    stars = int((i/hght) * base)
    print('*'*stars)