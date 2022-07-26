from animal import Animal

'''
By putting Animal in the () for the class, we are inheriting Animal class
to the Fish class.
super.__init__() needs to be added in the __init__ constructor.
'''
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # We are appending the behaviour of breathe by animal for a fish.
    def breathe(self):
        super().breathe()
        print("doing under water.")

    def swim(self):
        print("Moving in water!")