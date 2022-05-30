# Function that returns a boolean if the word secret is in a string

def secret_checker(my_string):
    return 'secret' in my_string.lower()

print(secret_checker(input('Enter a sentence')))

    '''
        OR
        
    # my_string = input('Enter a sentence')
    if 'secret' in my_string:
        return True
    else:
        return False
        
print(secret_checker(input('Enter a sentence')))
'''