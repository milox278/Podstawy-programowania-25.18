###
# A program that prints your height both in cm and in feet and inches.
#
cm =int(input("Enter your height in cm: "))

feet = cm * 0.032808399
inches = cm / 2.54
# calculate the number of feet

print(f'I am {cm}cm tall, which is {feet:.2f} feet and {inches:.2f} inches.')