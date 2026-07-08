def luckyDraw(names,number_of_participants):
    #Lucky Draw System
    '''
    - Input from the user (number of participants)
    - Input number of participant's name in a list
    - shuffling the list
    - generate first, second, and third winners [0], [1], and [2]
    - use python function and return with unpacking mechanism of tuple
    '''
    from random import shuffle
    shuffle(names)
    return names[0],names[1],names[2]

number_of_participants=int(input("Enter number of participants : "))
names=[]
for i in range(number_of_participants):
    name=input(f"Enter name of participant {i+1} : ")
    names.append(name)

winners=luckyDraw(names,number_of_participants)
i=1
for winner in winners:
    print(f"winner {i} : {winner}" )
    i+=1