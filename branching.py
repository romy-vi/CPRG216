# primitive data types

x = 2 # int
y = 3.4 # float 
z = "Hello" # string

condition = True # Boolean

# values of an expression or statement 

name = input("Enter your name: ") # Does this have a value (output)
age = 2025 - 2007

# Boolean Expression
# We are trying to answer a question 
# the answer is either "yes" or "no" (True or False)
# our answer to this question is the value of the expression

3>4 # is this a boolean expression?
# We are asking if 3 > 4 ??? The answer is no (False)
# Then the value of this expression is what?

var = 3 >4 # Logical expression 
#what is the type of var? Boolean

print("Var is type", var)

# choosing the variable name 
# by convention people use a question for the variable name of 
# a boolean expression 

is_adult = age>= 18

# provide three variable names for boolean variable 
is_even = (age %2 == 00) # equality check operator # % = remainder
print(is_even)
# Logicall operators > < >== <== == 

is_absent = True
is_child = False

won = False

# List the logical operations 
# Larger then >
# Larger than or equal >=
# Smaller than <
# Smaller than or equal <=
# Equal ==
# not equal !=

print("is 3>4?", 3> 4)
print("is 3<=4?", 3<=4)
print("is 3 equal to 5?", 3==5)
print("is 5 >= 5?", 5>=5)
print("is age larger than 18?", age>18)
print("are 4 and 5 not equal?", 4 !=5)

# Now let's work on if statement 
# if (keyword, is a must)
# boolean expression (is a must)
# : (is a must)
# indentation (must have)
# one or more statements of any type 
# non indented else (optional)
# : (is a must after else)
# one or more statements (is a must if you use else)

if 3<4: # : is like then what?
    print("yes")
    print("Yes that is true")
print("Outside if statement")

# What is statement? the smallest section of code complete instruction 
if 4>5:
    print(True)


# Now let's work on else statement 
# if (keyword, is a must)
# boolean expression (is a must)
# : (is a must)
# indentation (must have)
# one or more statements of any type 
# non indented else (optional)
# : (is a must after else)
# one or more statements (is a must if you use else)



# Now let's work on if elif else statement 
# if (keyword, is a must)
# boolean expression (is a must)
# : (is a must)
# indentation (must have)
# one or more statements of any type 
#one or more of the following
    #elif (optional)
    # condition (mandatory if you have elif)
    # : 
# non indented else (optional)
# : (is a must after else)
# one or more statements (is a must if you use else)