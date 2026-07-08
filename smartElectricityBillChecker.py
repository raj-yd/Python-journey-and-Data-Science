units = int(input("Enter electricity units consumed: "))

if units <= 100:
    print("Low Consumption")
elif units <= 300:
    print("Moderate Consumption")
else:
    print("High Consumption")