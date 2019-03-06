# rock paper scissors
# it's a game. - Riley McGuire

import random

response = 0
prompt = """
[1] - Rock
[2] - Paper
[3] - Scissors
"""
print(prompt)  # print the var made above
possibleresponses = [1,2,3]

response = int(input("Choose one: "))

while response not in possibleresponses:
    #try:
        print("ERROR: That's not a choice")
        response = int(input("Choose one: "))
    #except:
        #print("ERROR: you gotta enter a number fam")

rps = ''

if response == 1:       rps = 'rock'
elif response == 2:     rps = 'paper'
elif response == 3:     rps = 'scissors'

cresponse = random.randint(1,3)

crps = ''
if cresponse == 1:      crps = 'rock'
elif cresponse == 2:    crps = 'paper'
elif cresponse == 3:    crps = 'scissors'

result = "TIE"

if rps == 'rock':
    if crps == 'paper':         result = 'LOSS'
    elif crps == 'scissors':    result = 'WIN'

if rps == 'paper':
    if crps == 'rock':          result = 'WIN'
    elif crps == 'scissors':    result = 'LOSS'

if rps == 'scissors':
    if crps == 'rock':         result = 'LOSS'
    elif crps == 'paper':      result = 'WIN'

print("\n\n----------RESULTS----------")
print("YOU:\t\t"+rps.upper())
print("PC:\t\t"+crps.upper())
print("RESULT:\t\t"+result)

input("\n\n\nPress enter to continue.")
