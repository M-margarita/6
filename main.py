def rot(nums):
    nums = [i for i in str(nums)]
    
    for i,num in enumerate(nums):
        
        if num == '6':
            nums[i] = '9'
            break
    
    return int(''.join(nums))
