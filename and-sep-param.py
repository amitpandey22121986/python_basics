'''
end is the parameter of python's built-in print() function. 
It controls what should be printed at the end of print method. 
By default print statement ends with a newline (end='/n'). 
we can specify any string, special characters, or any escape sequences.

'''

# 'end'

A = "Course Data Science with Python"
B = "GeeksforGeeks"
# it will add at in the end of string A
print(A, end=' at ')
print(B)
# it will add @ in the end of string A
print(A, end=' @ ')
print(B)

'''

The sep parameter is used to specify the separator between the values that 
are passed to the print() function. By default print() uses a space character 
as the separator between values.

'''

# 'sep'
# these values will be sep by "-" and at will be added in the end
print("Course", "Data", "Science", "with", "Python", sep='-', end=' at ' )
print(B)
# A and B will be seperated by '\n' (new line)
print(A, B, sep='\n')