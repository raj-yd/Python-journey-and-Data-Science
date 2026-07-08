import os
#the library for files/directory related

# current working directory, where your current file is running
print(f"os.getcwd() = {os.getcwd()}")

#list all the files and folders in the current directory
print(f"os.listdir() = {os.listdir()}")
# print(len(os.listdir()))
all_dir=os.listdir()
print(type(all_dir))
# print(len(all_dir))
#how to create a new directory
os.makedirs("trailDirectory",exist_ok=True)
print("Directory created!!!!!")

#check whether the path exists or not
print(f"os.path.exists('demo.py') = {os.path.exists("demo.py")}")

path=r"C:\Users\raj\Documents\data.csv"  # r lagane se escape characters ignore ho jate hain
print("os.path.basename(path) = ",os.path.basename(path))  #data.csv
print("os.path.dirname(path) = ",os.path.dirname(path))  #C:\Users\raj\Documents

#joining paths
full_path=os.path.join("raj","desktop","documents","hello.txt")
print(f"full_path={full_path}")