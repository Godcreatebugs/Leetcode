"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

#solution 1 : 
"""
The one approachg thats not allowed here is to take a product of each element 
divide it and replace inplace of original array

Time complexity - Iterate through opnce and second iteration divide by ele itself
so O(n)
Space complexity is constant -O(1) - we are repalcing elements in place

NOTE:
this approach will fail when you have 0 as one of the element, we cant divide by that element

but we can code fort that special case
"""

#solution 2:
"""
this is a radical idea but lest say we have left product array 

so for element 1 is element 1 in this new LP(left product array) and I will
keep multiplying new elements and save it 

do same for Right side but start in reverse order

then multiply both array and replace in place 

-- Time Complexity - O(n) - since to make RP and LP and again using for loop
-- Space Complexity 2 * O(n) - to store LP and RP 

"""

# approach 3:
"""
now follow up question can we get rid of LP and RP and still achieve same results
techincally in left product array only element missing is right corrospnding element 

[1,2,3,4] -> results LP is [1,1,2,,6]-> so just multiplying n-1 to this array 
will give result we want
again space complexity also remains same just a cleaner way 
"""

class Solution:
    def __init__(self,arr) -> None:
        self.arr = arr
    
    def productEceptitself(self) ->list:
        product = 1
        arr = self.arr
        res = []
        n = len(self.arr)
        counter_zeros = 0
        for i in arr:
            if i==0:
                counter_zeros += 1
            elif i==0 and counter_zeros>1:
                product = 0     
            else: 
                product *= i
            
        #edge case where product is o [1,2,0]


        #now divide and replace each element in place

        #if we are not replacing element in place    
        # for i   in range(len(arr)):
        #     res.append(int(product / self.arr[i]))

        # use this for loop to avoid using extra space
        for i in range(n):        
            if self.arr[i] == 0 and counter_zeros:
                if counter_zeros > 1:
                    self.arr =[0] * n
                    return self.arr
                else:
                    self.arr =[0]* n
                    self.arr[i] = product
                    return self.arr

            self.arr[i] = int(product/self.arr[i])
            
                         
        return self.arr
    
    def productExceptitself(self)->list:
        #make left and right product array
        leftProduct = []
        rightProduct = []

        n = len(self.arr)
        #populate the arrays
        product = 1
        for ele in self.arr:
            leftProduct.append(product)
            product *= ele

        #right product side
        product = 1
        for ele in self.arr[::-1]:
            rightProduct.append(product)
            product *= ele
        rightProduct.reverse()

        for i in range(n):
            self.arr[i] = leftProduct[i] * rightProduct[i]

        return self.arr                

    def productExceptitselfOptimum(self)->list:
        #to store the result
        n = len(self.arr)
        res = []
        product = 1
        for i in range(n):
            res.append(product)
            product *= self.arr[i]

        #now we just multiply last elements corrospindly
        for i in range(n):
            res[i] = res[i] * self.arr[n-i-1]

        #return res
        return res                
            




    
    
#intialize the subject 

obj1 = Solution([3,1,2])

# print(obj1.productEceptitself())
# print(obj1.productExceptitself())
print(obj1.productExceptitselfOptimum())