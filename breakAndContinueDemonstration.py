# Problem Statement
# 1. Print numbers from 1 to 20.
# 2. Skip multiples of 3 using continue.
# 3. Stop execution when 15 is reached using break.

for i in range(1,21):
    if i==15:
        break
    if i%3==0:
        continue
    print(i)