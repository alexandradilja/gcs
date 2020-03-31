# is_prime function definition goes here
    
my_num = int(input("Input an integer greater than 1: \n"))

# Call the function here and print out the appropriate message
#hvernig finn ég prím tölur ???
def is_prime(num):
    if num == 2:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True

out = is_prime(my_num)
if out == True:
    print(my_num,'is a prime')
else: 
    print(my_num, 'is not a prime')
            

