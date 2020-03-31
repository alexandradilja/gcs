# The function definition goes here

my_num = int(input("Enter a number: "))

# You call the function here

def in_range(num):
    if 1<num<555:
        return True
    else:
        return False 

out = in_range(my_num)
if out == True:
    print(my_num,'is in range.')
else:
    print(my_num,'is outside the range!')