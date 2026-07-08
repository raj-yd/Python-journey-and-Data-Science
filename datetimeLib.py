import datetime
#accessing today's date
today=datetime.date.today()
print(f"Todays date = {today}")

#operations on datetime
#suppose, there is an event in future, and we want to caluclate how many days are left from the current day

event_date = datetime.date(2026, 7, 19)
days_left = (event_date - today).days
print('days_left', days_left)

#Assignment
#calculate your age

def age_Calculator(your_DOB):
    current_Date=datetime.date.today()
    # print(current_Date)
    age=(current_Date-your_DOB).days
    years=age//365
    print(f"Your age is = {years}")

# age_Calculator(3)
your_DOB=datetime.date(int(input("Enter Year : ")),int(input("Enter month : ")),int(input("Enter Date : ")))
age_Calculator(your_DOB)