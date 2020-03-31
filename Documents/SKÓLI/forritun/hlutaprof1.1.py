#Tek inn input fyrir manuð og input fyrir dag, capitalizea mauðinn 
# ef að dagurinn er einn af hatiðardögunum prentst hvaða hatiðar dagur annars ,,Not a holiday"

month = str(input('Month: '))
day = str(input('Day: '))
holiday = ''
month = month.capitalize()
holiday = month+' '+day
#'{}{:>1}'.format(month,day)
if holiday =='January 1':
    print("New year's day")
elif holiday == 'June 17':
    print('National holiday')
elif holiday == 'December 25':
    print('Christmas day')
else:
    print('Not a holiday')