
try:
    with open('okay.txt','r') as file2:
        contents=file2.read()
        print(contents)
except FileNotFoundError as e:
    print(f"Error - {e}")