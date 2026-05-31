class Animal:
    def __init__(self):
        self.eye = 2
    
    def leg(self):
        print("it have 4 legs!")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def wt(self):
        print("she is a crazy one!")
    def leg(self):
        super().leg()
        print("got eight leg")
    

momu = Cat()
momu.wt()
momu.leg()
print(momu.eye)
# momu.eye()