import csv
with open("students.csv","r") as file:
    dictCSV=csv.DictReader(file)
    #reading each row as a dictionary
    print(dictCSV) #execpting that it is single dictionary, but it holds multiple dictionaries (for each row), where each value is associated with its key (first row of the file)

    for row in dictCSV:
        #print(row)
        print(f'{row["name"]},{row["age"]},{row["marks"]},{row["city"]}')