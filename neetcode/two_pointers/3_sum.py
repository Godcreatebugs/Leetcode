"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""
"""
NOTE:
One thing to remember here is sorting will make 2 things easier
Skipping duplicate elements as combination should occur just once
and time complexity will be o(nlog(n)) and worst time case here is O(n^2) so 
it does not impede perfortmance of algorithm
since taking a dictionary approach or two pointers wil;l still result iterating at least 
twice
"""

#approach 1:
"""
sort element and then use two sum(with dictionary) to find an offset element

One very imporatnt tip: 
Even though you want to take dictionary approach you will still loop over 3 times 
and hence not wise to use that method to find complement
and rather better to approach with 2 pointer.

When you find element, update both right and left pointer simultanously, otherwise

[-1,0,1,1] - will give you wrong answer
even though you are updating pointers there is chance for duplicate to creep in 
and in that case before adding elements to last list make sure that elemenet 
is not present.
"""

            

def three_sum(arr):
    n = len(arr)
    if n <3:
        return []
    if n ==3:
        if (arr[0]+arr[1]+arr[2]==0):
            return[[arr[0],arr[1],arr[2]]]
        else:
            return []
    arr.sort()
    res=[]
    for i in range(n-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        current = arr[i]
        elements_found = []
        left = i+1
        right = n-1
        while(left<right):
            if(current+arr[left]+arr[right]>0):
                right -=1
            elif(current+arr[left]+arr[right]<0):
                left +=1
            else:
                elements_found = [current,arr[left],arr[right]]
                left +=1
                right -=1
                #make sure duplicates dont get copied over
                if elements_found in res:
                    continue
                res.append(elements_found)

    return res

print(three_sum([-2,0,0,2,2]))
        


    


