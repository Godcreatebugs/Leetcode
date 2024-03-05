"""
found a solution to check if duplicate exist or not 
This solution will be used to find which element was repeated

"""

#Approach 1: 
"""
just brute force and see for each element the other element is present or not.
Time Complexity - O(n^2) - we are iterating over nums twice essentially
Space Complexity O(1) - no extra space is needed

"""
def findDuplicate(nums):
    n = len(nums)
    for i in range(n):
        ele_i = nums[i]
        for j in range(i+1,n):
            if ele_i == nums[j]:
                return nums[i]
    return -1 

#test cases 
# print(findDuplicate([1,2,3,4]))   #-> return -1
# print(findDuplicate([1,2,3,3]))   #->return 3  

#Approach 2 : Use Hash map
"""
go over ele and make a whole list and check value of each key , 
if value >1 then  return key
Time complexity - O(n) - to iterate twice on array
Space complexity - O(n) - to store hash map

"""

def findDuplicateMap(nums):
    n = len(nums)
    nums_dict = {}
    for num in nums:
        if num in nums_dict and nums_dict[num] >= 1:
            return num
        nums_dict[num] = nums_dict.get(num,0) + 1
    return -1

print(findDuplicateMap([1,2,3,2]))

