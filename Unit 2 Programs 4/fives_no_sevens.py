# fives no sevens
# riles

x = 0
while x <= 125:
    if x % 5 == 0:
        if x % 7 != 0:  # no sevens allowed
            print(x, end=" ")
    x += 1
input("\n\nHit enter.")
