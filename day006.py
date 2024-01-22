from Poketmon import*


select = input('자신의 포켓몬을 선택하세요! 1) 파이리 2) 꼬부기 3) 이상해씨: ')
if select == '1':
    p1 = Pairi('파이리')

elif select == '2':
    p1 = Ggobugi("꼬부기")

elif select == '3':
    p1 = Isanghae_Ssi("이상해씨")

else:
    Poketmon.exception()

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
            Poketmon.exception()

    elif   behavior == '2':
        print('도망을 시도합니다!')
        i = random.randint(1,10)
        if i > 5:
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
            Poketmon.exception()

    elif behavior == '2':
        print('도망을 시도합니다!')
        i = random.randint(1,10)
        if i > 5:
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
            Poketmon.exception()
    else:
        Poketmon.exception()

    if e3._health > 0:
        print('적이 공격을 가합니다.')
        e3.skill3(p1)

print(f'축하합니다! {e3.get_name()}를 처치했습니다!')
print('과제 완료!!!')





