# Function that replaces the vowels in a string with a x

def code_maker(string):
    
    output = list(string)
    
    for index, letter in enumerate(string):
        for vowel in 'aeiou':
            if letter.lower() == vowel:
                output[index] = 'x'
                
    output = ''.join(output)
    return output
        
print(code_maker('Shola'))
            