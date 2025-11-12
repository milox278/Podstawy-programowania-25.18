###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input("Enter SWIFT code: ")
bank_code = swift[0:4]
country_code = swift[4:6]
location_code = swift[6:8]
branch_code = swift[8:11] if len(swift) == 11 else "N/A"
  
print(f"Bank code: {bank_code}")
print(f"Country code: {country_code}")
print(f"Location code: {location_code}")
print(f"Branch code: {branch_code}")
