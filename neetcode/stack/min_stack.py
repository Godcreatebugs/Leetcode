"""
155: MIN STACK

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the minStack.stack class:

minStack.stack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["minStack.stack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
minStack.stack minStack.stack = new minStack.stack();
minStack.stack.push(-2);
minStack.stack.push(0);
minStack.stack.push(-3);
minStack.stack.getMin(); // return -3
minStack.stack.pop();
minStack.stack.top();    // return 0
minStack.stack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin

"""

#approach 1:
"""
Understanding of a question 

pop, push and top will be a constant time operation as those are
index based operation

now coming back to question for obtaining the min elements
- since we are initalizing stack always and then start pushing 
the basic  idea is when you are doing a push method. 
at very first the min eleme is the first ele pushed
after second push we will compare local min and ele being pushed and 
if that element is less than ele already present in min we should replace that 

and every time we do push internally that element this method has to be executed 
and once the getMin methopd is called we basically 
call that extra variable
in this way with adding one extra variable we are keeping tack of min in constant 
time 

-- One other goo dpoint I found is we are eseentially altering the stack when 
using pop element,
So in this case I need a stack where I am also keeping track of previous min 


#edge case 1:
one of the edge case I have stuck on is [2,0,3,0]
-- and now if I start popping element my prev_min is still 2
but here we have two zeroes, so in current code if I dont put 

elif(self.minimum >= ele)
I will miss out on updating the prev_min() it will still point to 2 

so this took care but now I am hindered with another edge case

[2,0,3,0] - lets say I am popping all the element till only 2 is left 

since pop does not update prev_min I am stuck with [0,0] and get_min will give 
0 but the clear answer should be 2 

to handle this I have to check if only 2 elmenets are present and reset 
min and pre_min


"""
#this approach uses two seperate variable
class minStack:
    def __init__(self):
        self.stack =[] #intializse stack
        #intialize minimum from negative inf 
        self.minimum = float('-inf')
        self.pre_min = float("-inf")


    def pop(self)-> None:
        self.stack.pop() #return nothing just list removes the last ele 
        self.minimum = self.pre_min
        if len(self.stack) ==1:
            self.minimum = min(self.stack)


    def top(self)-> int:
        #returns top element of stack
        return  self.stack[-1]
    
    def push(self,ele)-> None:
        self.stack.append(ele)
        #if its first iteration update both min and pre_min to same new value
        if self.minimum == float("-inf"):
            #technically I should use replace premin to min even for first iteration
            self.minimum = ele
            self.pre_min = ele
        elif(self.minimum > ele):
            self.pre_min = self.minimum
            self.minimum = ele

    def get_min(self)-> int:
        print(self.minimum)
        return self.minimum  

minStack1 = minStack()
minStack1.push(-2)
print(minStack1.stack)
minStack1.push(0)
print(minStack1.stack)
minStack1.push(-3)
print(minStack1.stack)
print(minStack1.get_min()) # function execution
print(minStack1)
minStack1.pop()
print(minStack1.stack)
print(minStack1.top())  #function execution
print(minStack1.stack)  
print(minStack1.get_min()) # function execution
print(minStack1.stack)

#approach 2
"""
Use stack to keep track of mins
"""

class minStackOptimum:
    def __init__(self):
        self.stack =[] #intializse stack
        #intialize satck for mean
        #visualize first ele as prev_min and second ele as curr_min 
        self.min_stack= [float('-inf'),float('-inf')]
        


    def pop(self)-> None:
        self.stack.pop() #return nothing just list removes the last ele 
        self.min_stack[-1] = self.min_stack[-2]
        if len(self.stack) ==1:
            self.minimum = min(self.stack)


    def top(self)-> int:
        #returns top element of stack
        return  self.stack[-1]
    
    def push(self,ele)-> None:
        self.stack.append(ele)
        if(self.min_stack[-1] > ele):
            self.min_stack[-2] = self.min_stack[-1]
            self.min_stack[-1] = ele

    def get_min(self)-> int:
        return self.min_stack[-1]  
    

print(-2**-32,-2**-32)    


class min_stack_pragma:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack= []

    def top(self)->int:
        return self.stack[-1]

    def getMin(self)-> int:
        return self.min_stack[-1]

    def push(self,val:int):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack[-1] = val

    def pop(self)-> None:
        #one thing I learned is self.stack.pop(the first part will be always exceuted)
        # and if we have match we will remove that ele from min_stack two
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

