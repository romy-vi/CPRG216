'''
print("Hello, welcome to the party software")
name = input("Please enter your name:\n")
if name == 'Romy':
    name = 'Romy'
    


print("Welcome,", name)
print("To have a drink you need to provide your age")

age = int(input("What is your age?"))

is_adult = age >=18 

if is_adult:
    print("You are allowed to drink")
else:
    print("Sorry, you are a child")
'''

# if else works fine if we only have two conditions

print("Welcome to the grade system")
grade = int(input("Please enter your grade"))

if grade >= 90:
    letter_grade = 'A'
elif grade>= 80:
    letter_grade = 'B'
elif grade >=70:
    letter_grade  = 'C'
elif grade >=60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Your letter grade is", letter_grade)