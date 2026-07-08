import csv
with open("loginData.csv","a+",newline="") as file1:
    with open("loginData.csv","a+",newline="") as file1:
        file1.seek(0)
        dictCSV=csv.DictReader(file1)
        for data in dictCSV:
            print(data)