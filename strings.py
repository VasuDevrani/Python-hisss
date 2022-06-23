name = 'apnacollege'
# indexing in python is same as c++ strings

print(name.upper())
print(name.lower())
# find function returns the index of character or substring in the string, if it is absent then -1 is returned
print(name.find('c'))

# replacing character or substring in string
newName = name.replace('college', ' attack on titans')
print(newName)

# boolean function to check the presence in a string
print('T' in name)