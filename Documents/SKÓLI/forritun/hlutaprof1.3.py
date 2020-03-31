#tek inn tvær heiltölur þar sem önnur er upphafstala og hin er tala sem er bætt við í hverri lotu
#geri svo runu þar sem tölunum er breytt í streng og alltaf bætt við strenginn 
#þegar summa gildana nær er >= 100 stoppar loopan og prentar runu og summuna

value = int(input('Initial value: '))
step = int(input('Step: '))
my_sum = value
my_string = str(value)
while my_sum <= 100:
   value += step
   my_string = my_string+' '+str(value)
   my_sum += value
print(my_string)
print('Sum of series: ',my_sum)

