"""
19/11/2022

problem: Two Sum

author: Azamat Ortiqov
"""


def two_sum(nums, target):

    numbers = dict()

    for i,item in enumerate(nums):

        n = target - item

        if n in numbers:
            return [numbers[n], i]
        
        numbers[item] = i
    
    return []

a = two_sum([1,2,8,6,9,10], 15)
print(a)