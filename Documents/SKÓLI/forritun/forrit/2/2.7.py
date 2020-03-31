age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
price = float(30.0)
if age>=65:
    price = price*5
    print('The price for your admission is ', price, ' dollars.')
elif age<=5:
    price = 0.0
    print('The price for your admission is ', price, ' dollars.')
else:
    print('The price for your admission is ',price, ' dollars.')