'''Data types of a variable are interpreted at runtime and we don't have to initially declare it,that is why 
Python is called dynamically-typed language. It represents the kind of value that tells what operations can 
be performed on a particular data. Since everything is an object in Python programming, data types are actually 
classes and variables are instances (object) of these classes.'''


# 1. Numeric Types 


a = int(input('Enter integer number: '))
b = int(input('Enter integer number: '))

print(a+b)

# 2. Floating-Point Numbers (float)


a = float(input('Enter decimal number: '))
b = float(input('Enter decimal number: '))

print(a+b)

# 3. Complex Numbers (complex):

a = int(input('Enter number: ')) + 4j
b = int(input('Enter number: ')) - 5j 

print(a+b)