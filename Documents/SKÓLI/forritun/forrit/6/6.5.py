s = input("Input a string: ")
runa=''
for index,letter in enumerate(s):
    if letter.isdigit() == True:
        runa+=letter
        
print(runa)