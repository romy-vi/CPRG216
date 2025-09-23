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
'''
year_of_birth = input("Please enter your year of birth\n")
print("Your age is ",2025 - int(year_of_birth))
'''

# print function 
    # working with a separator 

print("Hello", "world", sep=' ', end=' ')
print("Hello", "world", sep=' ')
print("Hello\tworld")
print("Hello\nworld")
print('What is the student\'s name?')
print('Use this symbol \\ to make an escape character')

# precedence rules (order of operations, programming algebra)

expression = 3+4*0-300+12/3
print(expression)

expression = 4/2*3


# More about assignment 

x = 3 
x = x+5

print(x)

#can we have a shorthand for this expression?\

x += 5 # x = x+5
print(x)
# other expressions 
x -= 2 # x=-2
print(x)
x *= 3 # x * 3
print(x)
x /=2 # x = x/2
print(x)
x **=4 # x ** 4 
print(x)