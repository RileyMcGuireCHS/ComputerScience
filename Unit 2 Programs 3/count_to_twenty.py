# count_to_twenty.py 
# Riley McGGuire

num = 1
res = ""
while num < 21: # loop to 20
	res += str(num) + ", "
	num += 1
print(res.strip(", "))

input("\n\nPress enter to continue")
