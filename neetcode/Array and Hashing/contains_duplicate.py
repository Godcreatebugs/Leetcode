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

THIS APPROACH DO NOT WORK - YOU CAN TRY ANY WAY BUT SOMETIMES FOR BELOW LIST 
IT WILL PRODUCE WRONG RESULTS
"""

def containsDupls_xor(nums):
    # just going ovcer for loop and keeping xor updation wont give you right result

    seen_once = 0 
    seen_twice  = 0 

    for num in nums:
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~seen_once & (seen_twice ^ num)

        if seen_twice != 0:
            return True
    return False


# print(containsDupls_xor([1,2,3,4,5])) 


# approach 4: 
"""
Brute force the solution where we compare each element with every other ele 

Time complexity - O(n^2) - since we are iterating over the array essentially twice
Space Complexity - O(1) - we are not storing a comparison of ele, thats wiped out with each new teration
"""

def containsDuplicates_BF(nums):
    seen_twice = False
    n = len(nums)
    for i in range(n):
        ele_i = nums[i]
        #we are taking j from i + 1 becuase if duplicates were to be found we could have found in first iteration
        #[1,2,1,3] - this could have been foudn when i was 1 and we were iterating over j 
        for j in range(i+1,n):
            ele_j = nums[j]
            if ele_i == ele_j:
                return True
    return seen_twice


#test cases 
# print(containsDuplicates_BF(nums=[1,2,3,1]))

# print(containsDuplicates_BF(nums=[1,2,3,4]))

#approach 5: 
"""
Sort the ele and check next ele and if next ele is same then return True else False

Time complexity - O(nlog(n)) - quick sort algorithm and then O(n) to go over loop
Space complexity - O(1) - no space required
"""
def containsDuplicatesSort(nums):
    nums.sort()
    n = len(nums)
    for i  in range(n-1):
        if nums[i] == nums[i+1]:
            return True
        
    return False 

# test cases 
# print(containsDuplicatesSort([1,2,3,4,5]))   
# print(containsDuplicatesSort([1,2,3,4,1]))   

#approach 6:
"""
similar to approach number 2 but we are making set as we go and if ele is found in 
set already we return True else False

Time Complexity O(n) - while making set we are iterating over it just once 
Space Complexity O(n) - We need O(n) to store set 

"""

def containsDuplicateSetMake(nums):
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False

#test cases appraoch 6:
# print(containsDuplicateSetMake(nums=[1,2,3,4,5]))
# print(containsDuplicateSetMake(nums=[1,2,3,4,1]))


#approach 7: 
"""
similar to set we can use dictionary/hashmap where  we can see if ele is in dictionay and 
check if its there then check key >1 or not if yes return True else False

Time Complecity - O(n) - iterating just once in a loop
Space Complexity - O(n) - to store dictionary 
"""

def containsDuplicatesDict(nums):
    nums_dict = {}
    for num in nums:
        if num in nums_dict and nums_dict[num] > 1:
            return True
        nums_dict[num] = nums_dict.get(num,0) + 1
    return False    

print(containsDuplicatesDict(nums=[1,2,3,4]))        