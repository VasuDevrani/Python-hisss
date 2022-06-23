age = input("enter your age \n");
age = int(age)

# in c++ or java like languages we need to use curly brackets to maintain the if else regions but in python we just need proper intendation 
if age >= 18:
    print("hey you are an adult")
elif age<18 & age>3:
    print("just go to school")
else:
    print("hey little kid")

# intendation is like if we writing the statement without the tab gap then it'd not be considered under if else