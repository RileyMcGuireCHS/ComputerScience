# fortune_new
# it's magic  - Riley McGuire

import random

name = input("ENTER YOUR NAME: ")

fortuneInt = random.randint(1,8)

fortune = ''  # choose a fortune
if fortuneInt == 1:         fortune = 'You will live forever'
elif fortuneInt == 2:       fortune = 'You will not live forever'
elif fortuneInt == 3:       fortune = 'You will meet a famous rapper'
elif fortuneInt == 4:       fortune = 'Ask again later'
elif fortuneInt == 5:       fortune = 'No'
elif fortuneInt == 6:       fortune = 'Yes'
elif fortuneInt == 7:       fortune = 'You will be rich'
elif fortuneInt == 8:       fortune = 'You will be poor'

print(name + ", Your fortune is:")
print(fortune)

input("\n\nPress enter to continue")
