# This is our third class demo 
''' 
In this class we will work on 
variables, operators and other stuff 
'''
# Review
#assignment 

x = 5 # int
y = 4.5 # float
msg = "Hello" # string
condition = True # Bool
print("The value of the variable x is:", x, "and the type is:", type(x))
print("The value of the variable y is:",y, "and the type is:",type(y))
print("The value of the variable msg is:",msg, "and the type is:",type(msg))
print("The value of the variable condition is:",condition, "and the type is:",type(condition))

# some functions call : print, input, int, float, str, bool
num_as_text = "43"

num_as_num = int(num_as_text) # cnverting string (text) to num

print(num_as_text, type(num_as_text)) # will print as a text
print(num_as_num, type (num_as_num)) # will it print?
print(str(num_as_num)) # equivalent

num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_text = str(num2)


# Using input function.. Note input function always return to a string (text)

year_of_birth = input("Please enter your year of birth\n")
print("Your age is ",2025 - int(year_of_birth))


# problem 


user_input = input("Enter the radius of a circle")

area = 3.14 * user_input ** 2


print("The area of the circle is", area, type(area))

