class Fahim:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
fahim = Fahim('Fahim', 25)

fahim.display()