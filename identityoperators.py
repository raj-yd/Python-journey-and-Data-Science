#Performing identity operators , identity operators checks is memory is same or not
a=10
b=10
c=20
print(f"{a} is {b} = {a is b}")
print(f"{a} is not {b} = {a is not b}")
print(f"{a} is {c} = {a is c}")
print(f"{a} is not {c} = {a is not c}")
print(f"{a} is {100/10} = {a is 100/10}")
print(f"{a} == {100/10} = {a== 100/10}")