#tek inn mörg int þar til mínustala er slegin inn, geri það í while 
#ef nýr innsláttur er hærri en sá fyrri fær max gildi sama gildi og innslátturinn
#þegar mínustala er slegin inn prentast hæðsta gildið út

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = num_int 
while num_int>=0 :
    num_int = int(input("Input a number: "))
    if num_int>max_int:
        max_int = num_int
    
print("The maximum is", max_int)    # Do not change this line
