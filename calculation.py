print("+")
print("-")
print("*")
print("/")

# get the input 
num1= int (input("enter the first number : "))
num2= int(input("enter the second number : "))
Operator=input(" Enter the opeerator ")

# calculation base on operators
if Operator == '+' :
    print(f"answer is : {num1+num2}")
elif Operator == '-' :
    print(f"answer is : {num1-num2}")
elif Operator=='*':
    print(f"answer is : {num1*num2}")
elif Operator=='/':
    if num2!=0:
        print(f"answer is : {num1/num2}")
    else:
        print("cant devide by zero")
        
else:
    print("invalid operator")





