tree_circumference = float(input('Enter tree circumference in cm: '))
tree_diameter = tree_circumference / 3.14
tree_cut = tree_diameter >= 50
print(f'Tree diameter is {tree_diameter:.2f} cm')
print(f'Tree can be cut: {tree_cut}')