# Exercise 7: Function that returns the sum of list of integers if they are even
# and the value of the list when they are odd

def sum_or_list(mylist):
    
    if len(mylist) % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)

print(sum_or_list([1,2,3,4,5]))
    