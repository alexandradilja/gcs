i=1
while i <= 18:
    x_par = 'Par of hole ' + str(i) + ': '
    x_score = 'Score of hole ' + str(i) + ': '
    par = int(input(x_par))
    score = int(input(x_score))
    mis = (par - score)
    
    if mis < (-3):
        print('invalid score')
    if mis == (-3):
        print('albatross')
    if mis == (-2):
        print('eagle')
    if mis == (-1):
        print('birdie')
    if mis == 1:
        print('bogey')
    if mis == 2:
        print('double bogey')
    if mis == 3:
        print('triple bogey')
    if mis > 3:
        print ('bad hole')

    i+=1

