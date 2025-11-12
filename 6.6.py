characters_to_check = ['a', 'b', 'z', 'A', 'B', 'Z', '1', '=', '+', '€']
for char in characters_to_check:
    numerical_representation = ord(char)
    print(f'The character "{char}" has the numerical representation: {numerical_representation}')