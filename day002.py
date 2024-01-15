# #x = 2
# y = x + 5 #name 'x' is not defined
# print(y)

print(type(3.14))
print(type(3.14) == float)
print(isinstance(3.14, float))
print(isinstance(7, int))

artists = ['BTS' , '뉴진스', '핑클' , 'SES' , 'HOT' , '블랙핑크']
group = artists
print(artists , group)
artists[2] = '세븐틴'
print(artists , group)