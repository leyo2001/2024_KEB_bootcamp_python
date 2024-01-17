# 8.1
# e2f = dict(dog = 'chien', cat = 'chat', walrus = 'morse')
# print(e2f)

# 8.2
# e2f = { 'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
# print(e2f['walrus'])

# 8.3
# e2f = { 'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
# f2e = {}
# for key, value in e2f.items():
#     f2e[value] = key
#
# print(f2e)

# 8.4
# e2f = { 'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
# print(e2f['dog'])

# 8.5
# e2f = { 'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
# for key in e2f:
#     print(key, end = ' ')

# 8.6
# life = {'animals' :  {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
#         'plants':{} ,
#         'other':{}                                                        }

# 8.7
# life = {'animals' :  {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
#         'plants':{} ,
#         'other':{}                                                        }
# print(life.keys())

# 8.8
# life = {'animals' :  {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
#         'plants':{} ,
#         'other':{}                                                        }
# for i in life.keys():
#         print(i, end=' ')
#         for j in life[i].keys():
#                 print(j, end = ' ')

# 8.9
# life = {'animals' :  {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
#         'plants':{} ,
#         'other':{}                                                        }
# print(life['animals']['cats'])

# 8.10
# squares = {i : i*i for i in range(10)}
# print(squares)

# 7.1
# year_list  = [i for i in range(2001,2007)]
# print(year_list)

# 7.2
# year_list  = [i for i in range(2001,2007)]
# print(year_list[3])

# 7.3
# year_list  = [i for i in range(2001,2007)]
# print(year_list.pop())
# print(year_list[-1])

# 7.4
# things = ['mozzarella', 'cinderella', 'salmonella']

# 7.5
# things = ['mozzarella', 'cinderella', 'salmonella']
# for i in things:
#     print(i.title())
# print(things)

# 7.6
# things = ['mozzarella', 'cinderella', 'salmonella']
# print(things[0].upper())

# 7.7
# things = ['mozzarella', 'cinderella', 'salmonella']
# #things.pop()
# # del things[2]
# # things.remove('salmonella')
# print(things)

# 7.8
# surprise = ['Groucho', 'Chico', 'Harpo']

# 7.9
# surprise = ['Groucho', 'Chico', 'Harpo']
# surprise[2] = surprise[2].lower()
# print(surprise[2])
# new = ''
# for i in surprise[2]:
#     new = i + new
# surprise[2] = new.title()
# print(surprise)

# 7.10
# list1 = [i for i in range(10) if i%2==0]
# print(list1)

# 7.11
# start1 = [ 'fee', 'fie', 'foe']
# rhymes = [
#     ('flop', 'get a mop'),
#     ('fope', 'turn the rope'),
#     ('fa', 'get your ma'),
#     ('fudge', 'call the judge'),
#     ('fat', 'pet the cat'),
#     ('fog', 'walk hte dog'),
#     ('fun', "say we're done")
# ]
# start2 = 'Someone better'
#
#
# for i in range(len(start1)):
#     start1[i] = start1[i] + '! '
#     start1[i] = start1[i].title()
#
#
# for i in range(len(rhymes)):
#     print(''.join(start1) + rhymes[i][0].title()+'!')
#     print(start2, rhymes[i][1]  + '.' )








