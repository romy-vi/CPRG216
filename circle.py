# I want to compute the circumference and the area of the circle 
# assume the circle radius is 5
# modify : ask the user to enter the circle radius 
# and that pi = 3.14 


PI = 3.14
user_input = input("please enter the radius of the circle: ")
print("type user input ", type(user_input))


r = int(user_input)
circumference = 2 * PI * r
area = PI * r **2
print(circumference)
print(area)

