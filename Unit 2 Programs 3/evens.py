#evens.py by riley mcguire
# print evens
number = 100 # i needed a number
while (not number >= 0) or (not number <= 20): 
	number = int(input("ENTER A NUMBER: "))

while number:
	if not number % 2:
		print(number)
	number -= 1

input("\n\nPress enter to continue")