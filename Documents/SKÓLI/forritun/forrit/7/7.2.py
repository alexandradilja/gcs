# Your function definition goes here

user_input = input("Enter a string: ")

def find_in_input(txt):
    upper = 0
    lower = 0
    for i in txt:
        
        if i.isupper() == True:
            upper+=1
        elif i.islower() == True:
            lower +=1
    return upper,lower
# Call the function here
upper,lower  = find_in_input(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)
