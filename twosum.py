def two_sum(nums, target):

    numbers = dict()

    for i,item in enumerate(nums):

        n = target - item

        if n in numbers:
            return [numbers[n], i]
        
        numbers[item] = i
    
    return []

a = two_sum([2,2], 4)
print(a)