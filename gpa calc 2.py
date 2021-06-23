"""GPA CALCULATOR"""

dream_gpa = float(input('What is your dream GPA?: '))
courses_taken = int(input('Please enter the number of courses taken: '))

needed = 24
failed = 0
count_gradesum = 0
grade = 0
sumgrades = 0
taken_so_far = 0

count = courses_taken
while count > 0:
    
    count = count - 1
    grade = int(input('enter one grade: '))
    sumgrades += grade
      
    if grade < 4:
        taken_so_far = taken_so_far + 1
        failed = failed + 1
        count_gradesum = count_gradesum + grade
        
    elif grade >= 4:
        needed = needed - 1
        taken_so_far = taken_so_far + 1
        count_gradesum = count_gradesum + grade

calc1 = (count_gradesum/courses_taken)

'dream_gpa = int(grades/needed+failed)'

calc2 = ((dream_gpa*(failed + 24)) - sumgrades)/needed

print ("")
print ("Courses left to take: " + str(needed))
print ("Your GPA: " + str(calc1))
print ("For your dream GPA you need: " + str(calc2) + " avg per course")
