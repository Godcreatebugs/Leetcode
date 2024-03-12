"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

#approach 1: 
"""
we can create a stack here and check if closing para is found if found
we check previous element and see its matching the closing one and we 
pop both elements out untill no elements are left
if at last we have no elements left we can return True

else False 

TIP:
an important thing when you start finding closing para please compare to checkers' last ele, 
rather than i-1 of string itself,
in case you have reached last element
this will fail if you have something like '{[]}'

also there is a case
'((' here you will just keep appending and return last True 

in that case put a condition like 
if (len(set(list(a)))) ==1 - edge case where all elements are the same return False
and at last return true

there is anotehr edge case "(){}}{"
in this case checker is empty and hence you cant find -1 ele
to handle this we also check len of checker and if its zero we return false ins econd elif condition

another edge case 
'([' here both are openig para 
to handle this 

I think '((' this will be also handled if we only check if checker is empty or not 

Note: 
I can not think of any other sol for this problem other than stack 
Time complexity - O(n) - since we have to iterate the whole array

Space Complexity - O(n) - worst case scenario all open brackets and hence this 
space complexity
"""

def valid_para(a):
    checker = []
    n = len(a)
    #if the number of ele is odd return False
    if n % 2 != 0:
        return False

    
    for i in range(n):
        if a[i] in ['{','(','[']:
            checker.append(a[i])
        elif a[i] in ['}',']',')'] and i > 0 and len(checker)>0:
            if a[i] == '}' and checker[-1]=='{':
                checker.pop()
            elif a[i] == ']' and checker[-1]=='[':
                checker.pop()
            elif a[i] == ')' and checker[-1]=='(':
                checker.pop()
            else:
                return False
        else:
            return False        
    return len(checker) == 0 
# print(valid_para("(){}}{")) 

# approach 2: 
"""
Here we are using dictionary to pop matching para and match with stack last 
element and if they dont match return false
otherwise pop the element
"""
def valid_para_optimum(s):
    n = len(s)
    stack =[]
    match_dict ={'}':'{',')':'(',']':'['}
    if n %2 !=0 :
        return False
    
    for char in s:
        if char in '{([':
            stack.append(char)
        elif char in '])}' and len(stack)>0 and match_dict[char]==stack[-1]:
            stack.pop()
        else:
            return False    

    return len(stack) == 0


print(valid_para_optimum('[]'))