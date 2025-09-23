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


