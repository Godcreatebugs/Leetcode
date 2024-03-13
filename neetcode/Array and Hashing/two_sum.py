"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

#approach 1:
"""
brute force the solution and find complement in rest of the elements
if complement is found return the indices stored 

Time complexity - O(n**2) since finding the complement for each element also takes
O(n)
Space complexity is constant 
"""

def two_sum_bf(arr,target):
    n = len(arr)
    res =[]

    for i in range(n):
        complement = target- arr[i]
        if complement in arr:
            return [i,arr.index(complement)]
    return [-1,-1]


print(two_sum_bf(arr=[2,7,11,15], target = 9))


#appraoch 2:
"""
make a dcitionary and see iof complement is present, lookup time is constant 
so Time complexity is O(n) and Space complexity is O(n) to store hasmap/dict

well I think we have a problem here
- lets say array is [3,3] and target is 6, the hashmap wont allow to store duplicates

and hence we should store values other way around 
key should be index and vals should take values

I think to avoid this we have to populate the dictionary as we go 
by doing this if complment is found I will return current index and val from ahshmap 
"""
    
def two_sum_dict(arr:list,target:int)->list:
    n = len(arr)
    #dictionary to store element and its loc
    res = {}
    for i in range(n):
        complement = target-arr[i]
        if complement in res:
            return [i,res[complement]]
        res[arr[i]] = i 
    return [-1,-1]    

print(two_sum_dict(arr=[3,2,4], target = 6))