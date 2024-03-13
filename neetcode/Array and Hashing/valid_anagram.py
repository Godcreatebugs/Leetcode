"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
asdas


"""
#approach 1: 
"""
Just sort the strings and compare 
- Time complexity O(nlog(n)) - since this is using Tim sort 
and we are also occupying 2 O (n) space as well so linera time 
"""
def validAnagram_sort(s,t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t


#approach 2: 
"""
Make dictionary and traverse through dictionary to see if value macthes for keys
-- Time Complexity O(n) - traversing through dictioanry 
--Space Complexity 2O(n) - to store dictionary 

"""
def count_chars(s):
    n = len(s)
    res = {}
    for char in s:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1    
    return res    
        
def validAnagram_hashmap(s,t):
    if len(s) != len(t):
        return False
    dict_s = count_chars(s)
    dict_t = count_chars(t)
    for key in dict_s.keys():
        if key in dict_t and dict_s[key] == dict_t[key]:
            continue
        else:
            return False
    return True        


# approach 3:
"""
Make a frequence counter using unicode mapping for lower case alphabtes
(we can use this because the question specifically mentions we are given strings
of smaller alphabets)

increase counter when you are traversing first string and decrease when you 
traverse the second one 

and if count has non zero element return False

Time complexity same O(n)
Space complexity O(n) same 


"""

def validANagram(s,t):
    counter = [0]*26 

    for char in s:
        counter[ord(char)-ord('a')] += 1
    
    for char in t:
        counter[ord(char)-ord('a')] -= 1    

    for count in counter:
        if count != 0:
            return False
    return True

print(validANagram('abba',"baab"))        