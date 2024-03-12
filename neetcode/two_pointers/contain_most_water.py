"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""

#approach 1:
"""
seems like the only way to see it is two pointers
you take minimum hright in each iteration as height and 
distance bw 2 points as length and if we are excedding max are update that

Time complexity in this case will be O(n) - as we might have to go througfh loop in worst case
Space complexity is O(1) - no extra space needed
"""
def max_rain_water(arr):
    max_area = 0
    n = len(arr)
    l = 0
    r = n-1 
    
    while(l<r):
        height = min(arr[l],arr[r])
        gap = r-l
        area = height * gap 
        if area > max_area:
            max_area = area  
        if arr[l] > arr[r]:
            r -= 1
        if arr[l] <= arr[r]:
            l += 1      
    return max_area

print(max_rain_water([1,1]))

#approach 2:
"""
Just brute force the solution move left and rigth and update max_area when needed
Time complexity O(n^2) since we are moving with for loop 
Space complexity O(1) - just storing one variable
"""
def max_rain_brute(arr):
    max_area = 0 
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            height = min(arr[i],arr[j])
            gap = j-i
            area = height * gap 
            if area> max_area:
                max_area = area
    return max_area 

print(max_rain_brute([1,8,6,2,5,4,8,3,7]))            