#Important Functions of Strings 
a="i Need to buy apples, bananas, milk, and bread at the store"
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())

b="  Hello  i am here "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

c="Okay i am fine but i am not really fine"
print(c.replace("am","are"))
print(c.replace("i","you").replace("am","are"))

print(a.find("p"))
print(c.find("am fine"))
print(c.find("xyz")) # -1 return when value is not found

print(a.index("m"))
print(a.index("milk"))
# print(a.index("XYZ")) error

print(c.count("a"))
print(c.count("am"))
print(c.count("")) # len(c)+1
print(len(c))

d=c.split(" ")
print(d)

e=" ".join(d)
print(e)

f="Python"
print(f.startswith("Py")) #True
print(f.endswith("on")) #True
print(f.endswith("On")) #False

g="12345"
h="heyyy89"
print("______")
print(f.isalpha()) #True
print(g.isalpha()) #False
print(h.isalpha()) #False
print(f.isdigit()) #False
print(g.isdigit()) # True
print(h.isdigit()) #False
print(f.isalnum()) # True
print(g.isalnum()) #True
print(h.isalnum()) #True
i="heyy@09"
print(i.isalnum()) #False
print(f.isspace()) #False
print(a.isspace()) #False 
print(" ".isspace()) #True
print(a.swapcase())

j=f.center(15)
print(j)
print(f.center(15,"*"))
print(f.center(14,"-"))
k=f.zfill(15)
print(k)
print("42".zfill(10))