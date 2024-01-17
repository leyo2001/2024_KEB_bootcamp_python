sugang = dict(python='kim', cpp = 'sung', db='kang')
# print(sugang)
# sugang['datastructure'] = 'kim' # add
# print(sugang)
# sugang['datastructure'] = 'park' # update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('opensource'))
# print(sugang.get('opensource','not exist'))
for subject, professor in sugang.items():
    print(f'{subject} 과목  담당교수는 {professor}입니다')

for key in sugang:
    print(key)

for key in sugang.keys():
    print(key)

for value in sugang.values():
    print(value)

for item in sugang.items():
    print(item)
