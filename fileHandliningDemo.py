#python traditional version
#opening a file
file=open("notes.txt","r")
contents=file.read()
print(contents)
#it is very necessary to close any opened file before stoping execution, it avoids accident modifications/errors in your connected 
file.close() #but we can easily forget


#modern way for file handling using 'with' keyword
with open('notes.txt','r') as file2:
    contents=file2.read()
    print(contents)
    #now, no need to close() the file explicitly, with keyword will take care about your file