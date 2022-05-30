# Exercise 1: Function that takes in two numbers and returns true if their sum is equal to 10 and false if otherwise

def check_sum(n1, n2):
    return (n1 + n2) == 10:

print(check_sum(15, -5))

# Exercise 2: Function that takes in two numbers and returns true if their sum is equal to 10 and the sum value if otherwise

def sum_num(n1, n2):
    num_sum = n1 + n2
    if num_sum == 10:
        return True
    else:
        return num_sum

print(sum_num(15, 5))