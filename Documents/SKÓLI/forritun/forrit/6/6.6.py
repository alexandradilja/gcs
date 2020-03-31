name = input("Input a name: ")
first,last = name.split()
print(last[0].upper()+'.',first[0:1].upper()+first[1:-1].lower())