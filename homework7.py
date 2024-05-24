# Dictionary
my_dict  = {'Ivan': 1980, 'Sergey': 1988, 'Andrey': 1991, 'Marina': 1998}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Alexey'))
my_dict.update({'Sasha': 1979, 'Nastja': 2009})
del my_dict['Ivan']
print(my_dict)

# Sets
my_set = {2, 5, 2, 8, 3, 5, 4}
print(my_set)
my_set.update({'Play', (3, 4, 5)})
my_set.discard(5)
print(my_set)

