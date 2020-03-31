
# find_min function definition goes here
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

def find_min(num1,num2):

    if num1<num2:
        return first
    else:
        return second

minimum = find_min(first,second)
# Call the function here
print("Minimum: ", minimum)