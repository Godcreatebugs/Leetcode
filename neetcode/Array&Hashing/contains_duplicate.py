"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
#Approach 1: 
"""
make dictionary and see if any key has >= 2 value(occurance)
set flag to true and return it 

Time complexity - O(n) as we are iterating over a list once
Space complexity is o(n) - to store dictionary
"""
def containsDuplicates(nums):
    contains_dupl = False
    #make dictionary
    occur = {} 
    n = len(nums)
    for ele in nums:
        if ele not in occur:
            occur[ele] = 1 
        else:
            occur[ele] += 1

    print(occur)
    for val in occur.values():
        if val >= 2:
            contains_dupl = True
            return contains_dupl            
    return contains_dupl

#approach 2: 
"""
convert it to set and compare length of set and original list 
Time complexity - O(n) - we have to iterate over to create set
Space complxity -O(n) - to store a set temporily
"""

def containsDuplciate_set(nums):
    return len(nums) != len(set(nums))

# print(containsDuplicates([1,2,2]))
# print(containsDuplciate_set([1,2,2]))

#approach 3 
"""
Use xor operator which preserves diff number and if 
"""



