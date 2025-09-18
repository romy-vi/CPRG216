# variables
# variable has a name 
# , has a value
# , has an address
# , has a size
# , and has a type 

i = 3 # int
f = 4.5 # float 
b = True # boole 
s = "hello" 
msg = 'Hello world!'
ch = 'a' # it is still a string 

print(i, type(i))
print(f, type(f))
print(s, type(s))
print(msg, type (msg))
print(b, type(b))
print(ch, type(ch))

# variable names 
# can use  letters, digits, and underscore omly ( you can't have a comma in a name for example)
# it can start with a number 
# it can start with underscore but you shouldn't use it (because it has a different meaning)
# use meaningful variable names 

# example
circle_radius = 5
PI = 3.14
circle_radius =  6 # reassignment 
area_of_circle = PI * circle_radius * circle_radius

print(area_of_circle)
print("The area of the circle is")

# Operations 
a =  3+4 
b = 4-3
c = 4*3
d= 3/4
d_ = 3//4 # floor division
e = 4%3 # the result is the reamainder after division
f  = 3**3 # this is power (exponent)
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(d_, type(d_))
print(e, type(e))
print (f, type(f))

# combining  variables 

e = a+b # process the assignment from right to left 
# it means evaluate a+b first, then add the result to the variable e 

print("The value of e is", e)


#static type vs dynamic type 

x = 5 # type int 
print(x, type(x))
x = 4.3 # x changed its type to float 
print(x, type(x))
x = "Hello" # x changed to string 
print(x, type(x))
x = True # changed to Bool
print(x, type(x))

# casting 

x = 3    #int
y = 4    #int
z = x/y  #float, automatic casting 

print(z)

# manual casting (explecit casting)

int(z)
print(int(z))

print(int("43"))

print(str(43))

x = 1
print(x, type(x))

y = float(x)
print(y, type(y))

v = 4.3 
print(v, type(v))
u = int(v)
print(u, type(u))  #demotion 