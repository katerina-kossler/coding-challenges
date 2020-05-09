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
        
        
# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        '''
        takes a string of characters representing (J)ewels
        and a string representing the overall (S)tones
        
        records the number of Jewels found in the set of stones
        '''
        num_jewels = 0
        
        for stone in S: # O(n)
            if stone in J: # O(n)
                num_jewels +=1
                
        return num_jewels # O(n^2) solution
        
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        '''
        takes a string of characters representing (J)ewels
        and a string representing the overall (S)tones
        
        records the number of Jewels found in the set of stones
        '''
        num_jewels = 0
        
        # build set of jewels 
        jewels = set()
        for jewel in J:
            jewels.add(jewel)
        
        
        for stone in S: # O(n)
            if stone in J: # O(1)
                num_jewels +=1
                
        return num_jewels # O(n) solution
        
# Given an array of integers and an integer k, you need to find the total number of continuous
# subarrays whose sum equals to k.

# Example 1:
# Input:nums = [1,1,1,1,1], k = 2
# Output: 4

# Example 2:
# Input:nums = [1,1,-1,1,1], k = 2
# Output: 2

def find_matching_num_subarrays(nums, k): # still working on
    '''
    nums - array of intergers in the range [-1000,1000]

    k - integer to sum to
    '''
    count = 0
    for starting_idx in range(0, len(nums)):
        current_idx = starting_idx
        current_sum = nums[current_idx]
        if current_sum == k:
                count += 1
        for current_idx in range(current_idx+1, len(nums)):
            current_sum += nums[current_idx] 
            if current_sum == k:
                count += 1
    return count

print(find_matching_num_subarrays(
    [0,0,0,0,0,0,0,0,0,0],0)) 
    
# Given a binary tree, 
# return the inorder traversal of its nodes' values.   
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        inorder traversal == left,root,right
        
        
        assume: 
        - sorted BST
        - unique values in the tree
        '''
        
        # build up a list to represent a tree traversal
        traversal = []
        # examine (in order) the:
        while root:
            #1. left branch
            if root.left:
                traversal.extend(self.inorderTraversal(root.left))
                
            #2. root / current value
            traversal.append(root.val)
                
            #3. right branch
            if root.right:
                traversal.extend(self.inorderTraversal(root.right))
            
            return traversal      
            
# iterative
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        inorder traversal == left,root,right
        
        
        assume: 
        - sorted BST
        - unique values in the tree
        
          1
         2 3
        4 5

        >> [4, 2, 5, 1, 3]
        
            2
          3  null
         1 null
        
        '''
        visited = []
        # iterative
        nodes_to_visit = [] # list as a stack (last in, first out)
        # while going down, add to a stack
        while root or nodes_to_visit:
            while root:
                # add root to the stack and try proceeding left
                nodes_to_visit.append(root)
                root = root.left
            # when you can't go left, pop one off the stack, 
            root = nodes_to_visit.pop(-1)
            # add the value as visited 
            visited.append(root.val)
            # go right (and then try going left immediately after)
            root = root.right
        return visited
        

# We are given a list nums of integers representing a list compressed with 
# run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] 
# (with i >= 0).  For each such pair, there are freq elements with value val 
# concatenated in a sublist. Concatenate all the sublists from left to right to 
# generate the decompressed list.

# Return the decompressed list.

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 
# so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed_nums = []
        for index, num in enumerate(nums):
            if index % 2 == 1:
                new = [num] * nums[index-1]
                decompressed_nums.extend(new)
        return decompressed_nums
  
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...      

class Solution:
    def titleToNumber(self, s: str) -> int:
        columns = {
            'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,
            'I':9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26}
        column = 0
        for char in s:
            column *= 26
            column += columns[char]
        return column
        
# Make a function that prints the prime numbers 1 - 100
# Keep it simple 

# expanded mine for 1 - n where n >= 2 and is an integer

def print_prime(n):
    '''Prints prime numbers from 1 to n including n'''
    if is_integer(n) and n >= 2:
        divisible_by = []
        for number in range(2,n+1):
            prime = True
            for test in divisible_by:
                if number % test == 0:
                    prime = False
            if prime:
                print(number)
            divisible_by.append(number)
        
print_prime(100)

# pancake sort - make a flip function to flip the first k items in an array
# use flip to sort items in the array -- making a pancake sort
import math 

def flip(arr,k):
  '''takes in an array and reverses the order of the kth first elements'''
  # determine if k is valid: 0 to len(arr) - 1 
  if arr:
    # loop through indicies from 0 to the middle of the kth times rounded down
    halfway = int(math.floor((k+1)/2))
    for idx in range(0,halfway):
      # hold each item
      hold = arr[idx]
      # replace the item at the current position with it's opposite
      arr[idx] = arr[k-idx]
      # give the opposite position the value you held onto
      arr[k-idx] = hold
  
def pancake_sort(arr):
  '''Takes in an array and sorts using flip & returns the sorted array''' 
  # loop through items in the array and sort throughout
  if arr:
     for idx in range(len(arr)-1,0,-1):
        largest = 0
        for current in range(0,idx+1):
        # look for the largest value in each sized stack and flip there &
        # to the full current size of stack
          if arr[current] > arr[largest]:
            largest = current
        flip(arr,largest)
        flip(arr,idx)
  return arr
  
  
  
  # Move zeros to the end of a fized list array
  
  def moveZerosToEnd(arr):
	# brute force - likely higher complexity
    # goal: O(n) time complexity, O(1) space complexity
  
  # edit the org arr in-place
  
  if arr:
    # loop through array
    idx = 0
    zero_to_fill = 0
    
    while idx < len(arr)-1:

      if arr[idx] != 0:
        arr[zero_to_fill] = arr[idx]
        zero_to_fill += 1 
      idx += 1

    while zero_to_fill < len(arr)-1:
      arr[zero_to_fill] = 0
      zero_to_fill += 1 
      
  return arr

# arr = [1, 0, 0, 1, 0, 1]                
# arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]

# determine num filled orders
def filledOrders(order, k):
    '''
    takes in:
     1)an array of current orders (orders)
     2)the number of widgets available 
    -each element in the array denotes the number of widgets required
     for the order
    -assume priority is given to smaller orders as the goal is to 
     satisfy the highest number of orders
    '''
    # hold a variable for the number of orders we can satisfy
    num_filled = 0

    # sort the orders by increasing widget requirement
    order.sort() # O(nlogn)

    # loop through the sorted orders to count how many orders can be fullfilled
    for item in order: #O(n)
        if k >= item:
            num_filled += 1
            k -= item
        elif k < item:
            break
    return num_filled
    
    
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s 
#  2. STRING t
# both are space delimited strings of words, t is a sub string of t
# The function returns the words in string s that are not in t maintaining order

def missingWords(s, t):
    '''
    this function takes in two strings 
    with space delimited words and returns
    words that are present in the first 
    string (s) but are not present in the 
    second string (t) in an array 
    (maintaining the order they are in s)

    assume:
    - t is some ordered sub sequence of s
    - words do not need to be unique 
    (should not use python sets)
    - words are case sensitive
    - order matters ie: if first word is present in the second substring but out of order, the words do not match
    
    edge cases:
    - s or t are empty > return empty array
    
    current solution:
    s - s_words
    t - t_words
    m - non_match
    time - O(s) ~ O(n) 
    space - O(s + t + m) ~ O(s) ~ O(n)
    
    possible situations:
    - t sub string in begining of s
    - t sub string in middle of s
    - t sub string at end of s
    - t is empty ( assuming that's a valid substring )
    '''
    # hold an array for non-matching words
    non_match = []
    # break down strings into arrays using split
    s_words = s.split(" ")
    t_words = t.split(" ")

    # account for the edge case in which s or t are empty strings
    if s_words and t_words:
        # make a pointer to go through t's words
        t_idx = 0
        # loop through indices of s_words
        for s_idx in range(0,len(s_words)): # O(n) - n == length of s_words
            # if the words at both index's are equal, move both pointers
            if s_words[s_idx] == t_words[t_idx]:
                t_idx += 1
                # check if t_substring was done and add any remaining words in s_words
                if t_idx == len(t_words):
                    remaining_words = s_words[s_idx+1:]
                    non_match.extend(remaining_words)
                    # return the non_matching words
                    return non_match
            # if not, add the s word to non-match
            else:
                non_match.append(s_words[s_idx])
    # return the non-matching words
    return non_match
