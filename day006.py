class Pokemon:
    def __init__(self,name):
        self.name = name

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) 공격!')


class Pikachu(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

    def attack(self, target):
        print(f'{self.name}이(가) {target.name}을(를) {self.type} 공격!')

    def electric_info(self):
        print("전기 계열의 공격을 합니다.")

class Squirtle(Pokemon): # is - a
    pass

class Agumon:
    pass

p1 = Pikachu('피카츄','전기')
p2 = Squirtle('꼬부기')
p3 = Pokemon("아무개")
# print(issubclass(Pikachu, Pokemon))
# print(issubclass(Pokemon, Pikachu))
print(p1.name)
p1.attack(p2)
p1.electric_info()



