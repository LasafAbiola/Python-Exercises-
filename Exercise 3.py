# Exercise 5: Function that if given a sequence, that [1, 2, 3] is present in there

def seq_check(nums):
    
    for i in range(len(nums) - 2):
        
        if nums[i] == 1 and nums[i+1] == 2 and nums[i +2] == 3:
            return True
    
    return False

print(seq_check(7823456713))