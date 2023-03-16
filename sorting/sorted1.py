x = ['x', 'a', 'p', 'f', 'g', 'z']
print(sorted(x))

# Tuple
x = ('x', 'a', 'p', 'f', 'g', 'z')
print(sorted(x))

# String-sorted based on ASCII code
x = "python"
print(sorted(x))

# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print('Dictionary:', sorted(x,reverse=False))

# Set
x = {'x', 'a', 'p', 'f', 'g', 'z'}
print(sorted(x))

# Frozen Set
x = frozenset(('x', 'a', 'p', 'f', 'g', 'z'))
print(sorted(x))
