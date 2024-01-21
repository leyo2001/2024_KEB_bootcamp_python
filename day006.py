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

e = Poketmon('')


select = input('자신의 포켓몬을 선택하세요! 1) 파이리 2) 꼬부기 3) 이상해씨: ')
if select == '1':
    p1 = Pairi('파이리')

elif select == '2':
    p1 = Ggobugi("꼬부기")

elif select == '3':
    p1 = Isanghae_Ssi("이상해씨")

else:
    e.exception()

print('길을 갑니다')
e1 = Poketmon('적포켓몬1')
print(f'{e1.get_name()}을 만났습니다!')

while e1._health > 0:
    if p1._health <= 0:
        print('당신은 사망하였습니다.')
        exit()
    behavior = input('할 행동을 선택해주세요!\n1)공격 2)도망(등뒤의 상처는 검사의 수치다.) (성공확률 50%): ')
    if behavior == '1':
        attack = input(f'공격의 종류를 선택해주세요!\n1){p1._skill1}  2){p1._skill2}  3){p1._skill3}: ')
        print()
        if attack == '1':
            p1.skill1(e1)
        elif attack == '2':
            p1.skill2(e1)
        elif attack == '3':
            p1.skill3(e1)
        else:
            e.exception()

    elif   behavior == '2':
        print('도망을 시도합니다!')
        i = random.randint(1,10)
        if i > 5:
            print(i)
            print('빤쓰런성공!')
            p1.escape()
            break
        else:
            print('빤쓰런실패!')
            print('등뒤에 상처가 생겨 수치사했습니다.')
            exit()
    if e1._health > 0:
        print('적이 공격을 가합니다.')
        e1.skill1(p1)


print(f'{e1.get_name()}에게서 승리하였습니다!\n\n')
p1.victory()
print('길을 또 갑니다')
e2 = Poketmon('적포켓몬2')
print(f'{e2.get_name()}을 만났습니다!')


while e2._health > 0:
    if p1._health <= 0:
        print('당신은 사망하였습니다.')
        exit()
    behavior = input('할 행동을 선택해주세요!\n1)공격 2)도망(등뒤의 상처는 검사의 수치다.) (성공확률 50%): ')
    print()
    if behavior == '1':
        attack = input(f'공격의 종류를 선택해주세요!\n1){p1._skill1}  2){p1._skill2}  3){p1._skill3}: ')
        if attack == '1':
            p1.skill1(e2)
        elif attack == '2':
            p1.skill2(e2)
        elif attack == '3':
            p1.skill3(e2)
        else:
            e.exception()

    elif behavior == '2':
        print('도망을 시도합니다!')
        i = random.randint(1,10)
        if i > 5:
            print(i)
            print('빤쓰런성공!')
            p1.escape()
            break
        else:
            print('빤쓰런실패!')
            print('등뒤에 상처가 생겨 수치사했습니다.')
            exit()
    if e2._health > 0:
        print('적이 공격을 가합니다.')
        e2.skill2(p1)

print(f'{e2.get_name()}에게서 승리하였습니다!\n\n')
p1.victory()
print('마지막 길을 갑니다. 이번엔 심상치 않습니다...')
e3 = Poketmon('아카즈마 젠이츠')

while e3._health > 0:
    if p1._health <= 0:
        print('당신은 사망하였습니다.')
        exit()
    behavior = input('할 행동을 선택해주세요! 이제 도망이란 선택지는 없습니다.\n1)공격  ')
    if behavior == '1':
        attack = input(f'공격의 종류를 선택해주세요!\n1){p1._skill1}  2){p1._skill2}  3){p1._skill3}: ')
        print()
        if attack == '1':
            p1.skill1(e3)
        elif attack == '2':
            p1.skill2(e3)
        elif attack == '3':
            p1.skill3(e3)
        else:
            e.exception()
    else:
        e.exception()

    if e3._health > 0:
        print('적이 공격을 가합니다.')
        e3.skill3(p1)

print(f'축하합니다! {e3.get_name()}를 처치했습니다!')
print('과제 완료!!!')





