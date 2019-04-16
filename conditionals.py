# If/ Else conditions are used to decide to do something based on something being true or false

x = 10
y = 10

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x == y:
    print(f'{x} is equal to {y}')

if x>y:
    print(f'{x} is greater than {y}')
else:
    print(f'{x} is less than {y}')

# Logical operators (and, or, not) - Used to combine conditional statements


#new commits example

# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]
if x not  in numbers:
    print(x in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
    print(x is y)
