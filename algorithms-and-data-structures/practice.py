# 
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

#   example:
      # MinStack minStack = new MinStack();
      # minStack.push(-2);
      # minStack.push(0);
      # minStack.push(-3);
      # minStack.getMin();   --> Returns -3.
      # minStack.pop();
      # minStack.top();      --> Returns 0.
      # minStack.getMin();   --> Returns -2.

class MinStack:
    '''first in first out'''
    
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, x: int) -> None:
        '''add to the top of the stack'''
        
        self.data.append(x)
        if self.min:
            current_min = min(self.min[-1],x)
        else:
            current_min = x
        self.min.append(current_min)

    def pop(self) -> None:
        '''remove top element in the stack'''
        
        self.data.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        '''return top element in the stack'''
        
        return self.data[-1]

    def getMin(self) -> int:
        '''returns the smallest value in the stack'''
        
        return self.min[-1]

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(x)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()
 
 
#   
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice
#  in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # initialize an empty set
        seen = set()
        # loop through the list
        for num in nums:
            # for each item, check if in set
                 # if in set, return true
            if not num in seen:
                seen.add(num)
                # if not, add to set and continue
            else:
                return True
        # if full list entered is traversed return false
        return False
    
        # note: not just transforming list to set and comparing lengths
        # to save time if a match is found early in the list and to min
        # the required storage
            # quick set solution:
            # unique = set(nums)
            # return len(unique) < len(nums)
            
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]". 

class Solution:
  def defangIPaddr(self, address: str) -> str:
      new_address = ''
      for char in address:
          if char == '.':
              new_address += '[.]'
          else:
              new_address += char
      return new_address
      
class Solution: # same memory storage; faster; easier to understand
    def defangIPaddr(self, address: str) -> str:
        IP_parts = address.split('.')
        return '[.]'.join(IP_parts)