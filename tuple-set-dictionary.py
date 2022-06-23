marks = (1,2,3,4,2,2,2,2)
# tuples are like constant list that does not support any change
# made with round brackets
print(marks.count(2))
print(marks.index(3))

print("_______________________")

# sets contains only unique elements
# made with curly brackets
set1 = {1,2,2,4,6}
print(set1)
# cannot access values by index

for score in set1:
    print(score)

print("____________________________")

# dictionary is like c++ maps that stores key value pairs
mark = {"english" : 95, "chemistry" : 99}
print(mark["chemistry"]);

mark["physics"] = 100
print(mark)

mark["chemistry"] = 81

print(mark)
    
