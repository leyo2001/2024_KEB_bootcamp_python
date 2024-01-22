class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"

class NoFly(FlyingBehavior):
    def fly(self):
        return f'하늘을 날 수 없습니다.'

class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f'날개로 하늘을 훨훨 날아갑니다'

class JetPack(FlyWithWings):
    def fly(self):
        return f'로켓추진기로 하늘을 날아갑니다'




class SwimmingBehavior:
    def swim(self):
        return f"{self._Pokemon__name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name, hp, fly):
        self.__name = name
        self.__hp = hp
        self.fly_behavior = fly

    def set_fly_behavior(self, fly):
        self.fly_behavior = fly


    def attack(self):
        print("공격~")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    #name = property(get_name, set_name)


    #magic method
    def __str__(self):
        return self.__name + " 입니다"
    def __add__(self, other):
        #return self.__name + ' + ' + other.__name
        return f'두 포켓몬스터 체력의합은 {self.__hp + other.__hp}입니다.'



class Pikachu(Pokemon):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = NoFly() #composition


p1 = Pikachu('피카츄',35)
print(p1.fly_behavior.fly())





