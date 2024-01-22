import random


class Poketmon:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._escape_cnt = 0
        self._victory_cnt = 0
        self._skill1 = '약한공격'
        self._skill2 = '중간공격'
        self._skill3 = '벽력일섬'
    @staticmethod
    def turn_done(self):
            print(f'{self._name}턴 종료!\n\n')
    @staticmethod
    def exception():
        print('입력오류!')
        exit()
    def get_name(self):
        return self._name
    def escape(self):
        self._escape_cnt += 1
    def victory(self):
        self._victory_cnt += 1
        self._health = 100
    def skill1(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill1}(으)로 공격!')
        print(f'{enemy._name}이(가) 20의 데미지를 입었다!')
        enemy._health = enemy._health - 20
        print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)

    def skill2(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill2}(으)로 공격!')
        print(f'{enemy._name}이(가) 50의 데미지를 입었다!')
        enemy._health = enemy._health - 50
        print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)

    def skill3(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill3}(으)로 공격!')
        i = random.randint(1,10)
        if i >= 7:
            print(f'오의 발동!')
            print(f'아카즈마 젠이츠: 카미나리노 코큐... 이치노 카타 헤키레키 잇-센!')
            print(f'{enemy._name}이(가) 치명타를 입었다!')
            enemy._health = 0
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        else:
            print(f'오의 발동 실패..')
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)







class Pairi(Poketmon):
    def __init__(self, name):
        super().__init__(name)
        self._skill1 = '할퀴기'
        self._skill2 = '화염방사'
        self._skill3 = '연옥'

    def skill3(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill3}(으)로 공격!')
        i = random.randint(1, 10)
        if i >= 7:
            print(f'오의 발동!')
            print('렌고쿠 쿄주로: 호노노 코큐... 큐노 카나... 오기!!!! 렌고쿠!!!!!')
            print(f'{enemy._name}이(가) 치명타를 입었다!')
            enemy._health = 0
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        else:
            print(f'오의 발동 실패..')
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)

class Ggobugi(Poketmon):
    def __init__(self, name):
        super().__init__(name)
        self._skill1 = '몸통박치기'
        self._skill2 = '철벽'
        self._skill3 = '잔잔한 물결'
    def skill3(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill3}(으)로 공격!')
        i = random.randint(1,10)
        if i >= 7:
            print(f'오의 발동!')
            print('토미오카 기유: 미즈노 코큐 쥬이치노 카타.... 나기...')
            print(f'{enemy._name}이(가) 치명타를 입었다!')
            enemy._health = 0
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        else:
            print(f'오의 발동 실패..')
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)

class Isanghae_Ssi(Poketmon):
    def __init__(self, name):
        super().__init__(name)
        self._skill1 = '싸대기 때리기'
        self._skill2 = '씨 폭탄'
        self._skill3 = '명현주주'
    def skill3(self, enemy):
        print(f'{self._name}이(가) {enemy._name}을(를) {self._skill3}(으)로 공격!')
        i = random.randint(1,10)
        if i >= 7:
            print(f'오의 발동!')
            print('우즈이텐겐: 오토노 코큐! 고노 카타! 메-겐 소-소-! ')
            print(f'{enemy._name}이(가) 치명타를 입었다!')
            enemy._health = 0
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        else:
            print(f'오의 발동 실패..')
            print(f'{enemy._name}의 남은체력: {enemy._health}')
        self.turn_done(self)