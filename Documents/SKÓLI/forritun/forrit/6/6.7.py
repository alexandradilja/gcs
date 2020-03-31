#tek inn tölu tek // og deili aftur en safna %
my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code

kvot = my_int
leif = 0
bstr=''
if my_int != 0:
    while kvot >0:
        leif=(kvot%2)
        kvot=kvot//2
        bstr+=str(int(leif))   
    print("The binary of", my_int,"is", bstr[::-1])
else:
    print("The binary of", my_int,"is 0")