stars = int(input("Max number of stars: ")) # Do not change this line

for i in range(1,stars):
    stj = i*str('*')
    print(stj)
    stj += stj
for n in range(stars,0,-1):
    stj = n*str('*')
    print(stj)
    stj += stj
    