#línu með 10 format plássum með réttum einkennum þar sem hvert sæti hefur gildið margfalda með sæti og gildið eykst í hver skipti sem loopan er keuyrð


for i in range(1,11):
    value = i
    print('{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}{:>5}'.format(value*1,value*2,value*3,value*4,value*5,value*6,value*7,value*8,value*9,value*10))