import random as rd

def luckyDraw(participants):
    rd.shuffle(participants)
    return participants[0], participants[1], participants[2]

participant = [] #empty list

number = int(input('Enter number of participant (int)'))

for i in range(number):
    temp = input(f'Enter name {i+1}: ')
    participant.append(temp)

result = luckyDraw(participant) #unpacking
print('result: ', result)