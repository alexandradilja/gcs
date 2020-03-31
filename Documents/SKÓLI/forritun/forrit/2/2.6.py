d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line

# Fill in the missing code below
d_sum = d1 + d2
if 1<=(d1,d2)<=6:
    if d_sum == 7 or 11:
        print ('Winner')
    elif d_sum == (2,3 or 12):
        print('Loser')
    else:
        print(d_sum)
else:
    print('Invalid input')