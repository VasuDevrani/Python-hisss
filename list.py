arr = [1, 2, 3, True, "maths", 2, 2, 2]
print (arr)

for item in arr:
    print(item)

# bool is printed as it is
print(arr[3])

# in python unlike other languages negative indexes does mean index from the end of list
print(arr[-1])

# print(arr[-20]) inaccessible location in this case

# printing in range
print(arr[0 : 2])

# updating array from last
arr.append(99);

# insert at any position
arr.insert(0,20)

print(arr)

# bool to check presence of elements in array
print(99 in arr)

# length of list
print(len(arr))

i = 0;
while i< len(arr):
    print(arr[i])
    i += 1

print(arr.count(2))
print(arr.index(3))

arr.clear()
print(arr)

