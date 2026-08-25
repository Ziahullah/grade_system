
def studentgrademanager():
    try:
        score = float(input("Enter the student's score: "))
        if score >= 90 and score <= 100:
            grade = 'A'
        elif score >= 80 and score <= 89:
            grade = 'B'
        elif score >= 70 and score <= 79:
            grade = 'C'
        elif score >= 60 and score <= 69:
            grade = 'D'
        else:
            grade = 'E'

        print(f"The student's grade is: {grade}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

studentgrademanager()