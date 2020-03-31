# Your function definition goes here
def fibo(num):
    if num == 1:
        sequence = '1'
        return sequence
    elif num == 2:
        sequence = '1 1'
        return sequence
    else:
        num1 = 1
        num2 = 1
        sequence = '1 1'
        for i in range(2,num):
            num_sum = num1 + num2
            num1 = num2
            num2 = num_sum
            sequence += ' ' + str(num_sum)
        return sequence



n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
sequence = fibo(n)
print(sequence)