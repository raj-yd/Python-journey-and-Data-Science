marks=[int(i) for i in input("Enter marks of 5 subjects separeted by space : ").split()]
print(f"All marks - {sum(marks)}")
print(f"Highest marks - {max(marks)}")
print(f"Lowest marks - {min(marks)}")
print(f"Average marks - {sum(marks)/5}")