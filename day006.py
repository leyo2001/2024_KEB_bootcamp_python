# 10.1
# class Thing:
#     pass
# print(Thing)
# t = Thing
# print(t)

# 10.2
# class Thing2():
#     def __init__(self, letters):
#         self.letters = letters
#
# t = Thing2('abc')
# print(t.letters)

# 10.3
# class Thing3():
#     def __init__(self):
#         self.letters = 'xyz'
#
# t = Thing3()
# print(t.letters)

# 10.4
# class Element():
#     def __init__(self,name, symbol, number):
#         self.name, self.symbol , self.number = name , symbol , number
#
# e = Element('Hydrogen', 'H' , 1)
# print(e.name, e.symbol , e.number)


# 10.5
# class Element():
#     def __init__(self,name, symbol, number):
#         self.name, self.symbol , self.number = name , symbol , number
#
# el_dict = { 'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
# e = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])
# print(e.name,e.symbol,e.number)

# 10.6
# class Element():
#     def __init__(self,name, symbol, number):
#         self.name, self.symbol , self.number = name , symbol , number
#
#     def dump(self):
#         print(self.name, self.symbol, self.number)
#
# e = Element('a','b',1)
# e.dump()

# 10.7
# class Element():
#     def __init__(self,name, symbol, number):
#         self.name, self.symbol , self.number = name , symbol , number
#     def __str__(self):
#         return f'Element(name = {self.name}, symbol = {self.symbol}, number = {self.number} '
#
# hydrogen = Element('hydrogen','H',1)
# print(hydrogen)

# 10.8
# class Element():
#     def __init__(self,name, symbol, number):
#         self.__name, self.__symbol , self.__number = name , symbol , number
#
#     def name_getter(self):
#         return self.__name
#
#     def name_setter(self, new_name):
#         self.__name = new_name
#
#     name = property(name_getter, name_setter)
#
# hydrogen = Element('hydrogen','H',1)
# print(hydrogen.name)
# hydrogen.name = 'hy'
# print(hydrogen.name)
# print(hydrogen._Element__name)

# 10.9

# class Bear:
#     def eats(self):
#         return 'berries'
#
# class Rabbit:
#     def eats(self):
#         return 'clover'
#
# class Octothorpe:
#     def eats(self):
#         return 'campers'
#
# b = Bear()
# r = Rabbit()
# o = Octothorpe()
# print(b.eats(), r.eats(), o.eats())

# 10.10
# class Bear:
#     def does(self):
#         return 'disintegrate'
#
# class Claw:
#     def does(self):
#         return 'crush'
#
# class Smartphone:
#     def does(self):
#         return 'ring'
#
# class Robot:
#     def __init__(self, b , c, s):
#         self.b = b
#         self.c = c
#         self.s = s
#
#     def does(self):
#         print( self.b.does(), self.c.does(), self.s.does())
#
# b = Bear()
# c = Claw()
# s = Smartphone()
#
# r = Robot(b,c,s)
# r.does()


