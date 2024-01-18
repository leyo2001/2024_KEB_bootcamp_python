# 9.1
# def good():
#     return ['Harry', 'Rn', 'Hermione']
#
# print(good())

# 9.2
# def get_odds():
#     generator = (i for i in range(10) if i%2==1)
#     return generator
#
# for i in get_odds():
#     print(i)

# def get_odds():
#     for i in range(10):
#         if i%2==1:
#             yield i
#
# print(list(get_odds()))





# 9.3

# def test(f):
#     def new_add(a,b):
#         print('start')
#         r = f(a,b)
#         print('end')
#         print(r)
#         return r
#     return new_add
#
# @test
# def add(a, b):
#     c = a+b
#     return c
#
# add(1,2)

# 9.4
# n = int((input("Input number 0~2: ")))
# list1 = [0,1,2]
# try:
#     print(list1[n])
# except Exception as OopsException:
#     print('Caught an oops')










