"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

# we can leverage that the array is sorted and same as two sum buyt add 1 to the indices
# returning the answer

def two_sum_sorted(arr,target):
    n  = len(arr)
    left_p = 0
    right_p = n -1

    while(left_p< right_p):
        if arr[left_p] + arr[right_p] > target:
            right_p -= 1
        elif (arr[left_p] + arr[right_p] < target):
            left_p += 1
        else:
            return [left_p+1, right_p+1]


#a better way to right this
def two_sum_better(arr,target):
    right, left = len(arr) -1 , 0
    current_sum = arr[right] + arr[left]
    while current_sum != target:
        if current_sum < target: 
            left += 1 
        elif current_sum > target:
            right -= 1
        current_sum = arr[left] + arr[right]
    return[left + 1, right + 1]                    
print(two_sum_sorted([2,7,11,15],9))
print(two_sum_better([2,7,11,15],9))