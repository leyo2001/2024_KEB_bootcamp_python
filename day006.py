class FlyingMixin:
    def fly(self):
        return f'{self.name}이(가) 하늘을 훨훨 날아갑니다~'

class SwimmingMinxin:
    def swim(self):
        return f'{self.name}이(가) 수영을 합니다'


class Pokemon:
    def __init__(self, name):
        self.hidden_name = name

    def attack(self):
        print('공격~')

    def get_name(self):
        print("inside getter")
        return self.hidden_name

    def set_name(self, name):
        print("inside setter")
        self.hidden_name = name

    name = property(get_name, set_name)



class Charizard(Pokemon,FlyingMixin):
    pass

class Gyarados(Pokemon,SwimmingMinxin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

# print(g1.swim())
# print(c1.fly())
# c1.attack()
# #Charizard.attack() -> error
# Charizard.attack(c1)


# print(g1.name)
# g1.name = "잉어킹"
# print(g1.name)

# print(g1.name)
# print(g1.get_name())
# g1.set_name('잉어킹')
# print(g1.get_name())


# property
print(g1.name)
g1.name = '잉어킹'
print(g1.name)

