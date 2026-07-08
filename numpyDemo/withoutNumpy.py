marks=[80,56,78,90,79,88,78]
bonus_marks=[]
for i in marks:
    bonus_marks.append(i)

print(bonus_marks)

#alternative method - list comprehension

bonus=[i+5 for i in marks]
print(bonus)