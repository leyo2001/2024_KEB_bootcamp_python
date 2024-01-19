class Animal:
    def says(self):
        return 'I speak'

class Horse(Animal):
    # def says(self):
    #     return 'Neigh!'
    pass

class Donkey(Animal):
    # def says(self):
    #     return 'Hee Haw!'
    pass
class Mule(Donkey, Horse):
    pass

class Hinny(Horse, Donkey):
    pass


m1 = Mule()
h1 = Hinny()

# print(m1.says())
# print(h1.says())
print(Hinny.__mro__)
print(Mule.__mro__)






