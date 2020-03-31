
#153 is an Armstrong number because 1**3 + 5**3 + 3**3 = 153
top_num = int(input("Input a number between 0 and 999: "))
num_one = 0
num_two = 0
num_three = 0
for n in range (0,top_num):
    veldi = 0 
    if 0<=n<10:
        veldi= 1
    elif 10<= n <100:
        veldi = 2
    elif n>=100:
        veldi = 3