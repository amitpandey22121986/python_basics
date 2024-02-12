'''A dictionary in Python is an unordered collection of data values in form of key-value pairs. 
Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a 
Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.'''

dictionary = {'name':'amit','lastname':'pandey'}

print(dictionary,type(dictionary))
print(dictionary.get('name'))

dictionary = {1:'amit',2:'pandey'}

print(dictionary,type(dictionary))
print(dictionary.get(1))