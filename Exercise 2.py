# Exercise 3: Function that takes in a string and returns the first character of the string in uppercase

def first_upper(mystring):
    return mystring[0].upper()

print(first_upper('Tunde'))

# Exercise 4: Function that takes in a string and returns the last two characters of the string.
# If there are less than two characters return 'Error'.

def last_two(mystring2):
    if len(mystring2) < 2:
        output = 'Error'
    else:
        output = mystring2[-2:]
    return output

print(last_two('Messi'))