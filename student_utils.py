class PercentageError(Exception):
    pass
def calculate_percentage(marks_list):
    return sum(marks_list)/len(marks_list)
def get_grade(percentage):
    if percentage>100:
        raise PercentageError("Percentage is greater than 100")
    elif percentage <=100 and percentage > 80 :
        return "Grade - A"
    elif percentage <=80 and percentage > 60 :
        return "Grade - B"
    elif percentage <=60 and percentage > 40 :
        return "Grade - C"
    elif percentage <=40 and percentage >=0 :
        return "Fail"
    elif percentage <0 :
        raise PercentageError("Percentage Should not be negative")