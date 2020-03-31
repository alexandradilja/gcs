# palindrome function definition goes here

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
def palindrome(txt):
    
    out_str = ''
    txt = txt.lower()
    for letter in txt:
        if letter.islower() == True:
            out_str+= letter
    if out_str == out_str[::-1]:
        return True

    
    


out = palindrome(in_str)
in_str = '"'+in_str+'"'
if out == True:
    print(in_str,'is a palindrome.')
else:
    print(in_str,'is not a palindrome.')
