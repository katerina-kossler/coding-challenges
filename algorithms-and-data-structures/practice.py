
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
    
# find number of sock pairs
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    '''
    A function that takes in the total number of socks
    and an array denoting the 'color' of each sock as an integer

    the function returns how many pairs of sock there are

    assume:
    - valid inputs ie length of socks = len of color array
    edge cases:
    - 0-1 socks in the pile (0 pairs possible)
    - the color colors are denoted by integers 1-100 (limited search space)
    - maximum sock pile is 100 socks
    '''
    # form a variable to record how many pairs have been seen
    pairs = 0

    # check for edge case: 0-1 socks
    if n < 2:
        return pairs
    
        # form a dictionary for number of socks of each color
    socks_by_color = {}

    # loop through the array of socks
    for sock in ar:
        # check if the color has been seen and add one sock to the pair
        socks_by_color[sock] = socks_by_color.get(sock, 0) + 1
        # if the sock countfor this color is now even, inc the number of pairs
        if socks_by_color[sock] % 2 == 0:
            pairs += 1
    # after checking the available socks return the number of sock pairs that can be sold
    return pairs

# Count valleys in a hike
def countingValleys(n, s):
    '''
    A function that processes through a number of steps 
    and a string of the step was uphill or downhill

    Returns the number of valleys that were passed through
    
    def valley: 
    - begin at sea level
    - any number of steps below sea level
    - end when sea level is reached again

    assumptions:
    - hiker always starts and ends at sea level
    - at least two steps are taken per hike (at least 1 valley possible)
    
    edge case:
    - one step down and one step up (1 valley)

    focus for implementation:
    - record any time a new valley is entered 

    complexity:
    time: O(n) - n = length of s
    space: O(2) ~ O(1) = recording the valleys and altitude
    '''
    # make a counter for the number of valleys encountered
    valleys = 0
    # hold a variable to record the altitude relative to sea level
    altitude = 0
    # walk through steps:
    for direction in s:
        # if step is down
        if direction == 'D':
            # and the previous altitude was sealevel
            if altitude == 0:
            # increment the number of valleys
                valleys += 1
            # decrease the altitude
            altitude -= 1
        # if step if up
        else: 
            # increase the altitude
            altitude += 1
    # return the number of valleys
    return valleys


# Find minimum number of cloud jumps to win the game map (array)
def jumpingOnClouds(c):
    '''
    Takes in an array of integers representing clouds with
    0 for a safe cloud or 1 for a dangerous cloud

    Returns the minimum number of jumps required to reach the last cloud

    notes:
    - user can jump to a safe cloud that is 1 or 2 locations away from the 
    current position

    asummptions:
    - the first and last clouds are always safe to jump on
    - the map is always solvable: there is a safe cloud 1 or 2 locations away

    goal in solution:
    - prioritize further jumps if possible

    solution:
    time: O(n) : length of c (always moving forward by 1 or 2 spaces for cycle of loop)
    space: O(2) - O(2) : the jump counter and current cloud pointer 
    '''

    # record the number of jumps starting at 0
    jumps = 0
    # hold a pointer to the first position in the list of clouds
    cloud = 0
    # loop through until the end is reached (while)
    while cloud < len(c)-1:
        # check if you can jump two positions and if so, check if the cloud two away is safe
        if cloud < len(c)-2 and c[cloud+2] == 0:
            # if safe, move pointer up two
            cloud += 2
        # if either condition is not met, move to the next cloud
        else:
            cloud += 1
        # increase num jumps regardless
        jumps += 1
    # once loops exits (end is reached), return th enumber of jumps required 
    return jumps

# print the number of 'a' characters in the first n characters of the infinitely-
# repeating string s
def repeatedString(s, n):
    '''
    A function that takes in an 'infinitely-repeating' string s
    and the n number of characters to look through of s
    for instances of the character 'a'
    
    returns nothing and prints the number of times 'a' occurs in the first
    n characters

    assumptions:
    - n is 1 - 10^6
    edge cases:
    - no 'a's in the string > print 0
    - the base sequence for s is some length 1 - 100

    possible cases:
    - n is less than or equal to the first occurance of s
    - n is greater than the first sequence of s 

    solution:
    time: O(s+overflow) ~ O(n)
    space: O(3) ~ O(1)
    '''
    # initialze the number of a's seen to 0
    num_a = 0
    # if n == 0, print num_a and return None
    if n==0:
        return(num_a)
    # determine and hold the number of whole sequences of base s
    # are required for the first n characters
    whole_sequences = int(math.floor(n/len(s)))
    # and any overflow sequences of s to reach n
    overflow = int(math.floor(n % len(s)))
    # loop through the base s to determine how many 'a's are present
    for char in s:
        if char=='a':
            num_a+=1  
    # if 0, print 0 and return none
    if num_a==0:
        return(num_a)
    # multiple this number by the number of full loops of base s into
    # the number of 'a's seen
    num_a = num_a*whole_sequences
    # loop through the overflow characters of s for how many 'a's occur
    if overflow:
        for char in s[:overflow]:
            if char=='a':
                num_a+=1
    # print the number of 'a's in the nth first characters and return none
    return(num_a)
    

# Complete the hourglassSum function below.
def calculate_hourglass(arr, start_x, start_y):
    '''
    takes in a 2D array, an x and a y coordinate 
    returns the hourglass sum that begins at this location
    '''
    return (arr[start_y][start_x] +
            arr[start_y][start_x+1] +
            arr[start_y][start_x+2] +
            arr[start_y+1][start_x+1] +
            arr[start_y+2][start_x] +
            arr[start_y+2][start_x+1] +
            arr[start_y+2][start_x+2])

def hourglassSum(arr):
    '''
    Takes in a 2D array and returns the maximum
    hour glass sum in the array

    hour glass pattern:
    a b c
      d
    e f g

    assumptions:
    - the input array is always 6 x 6 (square)
    - the elements in the array are integers from -9 to +9

    edgecase:
    - all same value > return hourglass sum possible

    approach:
    - design algorithm to work with any square 2D array
    - move through array to valid start indices in x and y coords
    - calculate the hourclass sum and compare to current max
    '''
    
    # hold the maximum sum seen starting at neg inf
    max_hrglass = float('-inf')
    # determine the bounds for x and y indices based on array size [0 0 0 (0) 0 0]
    max_idx = len(arr)-2
    # walk through array by row
    for y in range(0,max_idx):
        # and column
        for x in range(0,max_idx):
            # at each valid index, calculate the sum
            new_hrglass = calculate_hourglass(arr, y, x)
            # compare to current max sum and keep the larger
            max_hrglass = max(max_hrglass,new_hrglass)
    # print the final largest sum
    return max_hrglass
    
# Complete the rotLeft function below.
# Rotate the array (a) by d places to the left
def rotLeft(a, d):
    '''
    Given an array of integers (a) and 
    a requested number of left rotations (d)

    Return the input array shifted d times
    
    Assumptions:
    - 1 < d <= len(a) at most the list will be fully rotated
    - 1 < len(a) < 10^5 (wide search space for size of array)

    Brute force solution: pop 1st item off the 
    front of the array and then append to the end of the array 
    (time: O(len(a)*d) ~ O(n^2))

    notes on arrays:
    - O(1): append / remove from end of the array

    current approach:
    - time: O(len(a)) ~ O(n) > going over every item in the array
    - space: O(n) > form a new list of same length
    '''

    # start a new array
    rotated = []
    # starting at the nth object into the array
    for ele in range(d,len(a)):
        # append to a new array
        rotated.append(a[ele]) 
        # note - would be same time and space to use
        # list.extend() on the same slice of the list
        # I chose a loop and append for increased clarity
    # starting from the beginning of the array
    for ele in range(0,d):
        # append all remaining objects to the array
        rotated.append(a[ele])
    return rotated
    
def num_of_paths_to_dest(n):
  '''
  Take in a size of grid (n)
  and return the number of paths
  
  - move up (N) or (E) at any one time
  - i >= j : (i,j)
  - we always start at (0,0)
  - we always end at (n-1,n-1)
  
  - equal up and east
  - 1 ≤ n ≤ 100: assume at least one path
  
  '''
  
  paths_to_loc = [[0 for i in range(n)] for j in range(n)]
  for y in range(n):
    for x in range(n):
      if x <= 1 and y == 0:
        paths_to_loc[y][x] = 1  
      elif x >= y:
        if x == 0:
          paths_to_loc[y][x] = paths_to_loc[y-1][x]
        elif y == 0:
          paths_to_loc[y][x] = paths_to_loc[y][x-1]
        else:
          paths_to_loc[y][x] = paths_to_loc[y-1][x] + paths_to_loc[y][x-1]
   
  return paths_to_loc[n-1][n-1]    

  # dynamic - number of, considering previous solutions 
        
  #F[n] = F[n-1] + F[n-2], F[0] = 1, F[1] = 2
  
  #num[row][col] = num[n-1,n] + num[n,n-1] 

  #num[1,1] = num[1,0] + num[0,1]
  #num[1,0] = num[0,0] = 1
  #num[0,0] = 1
  
# find max area for an array of container heights

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''Given a list of heights, 
            return the maximum area possible
        
        assumptions:
            - each side is one unit away from the next
            
        '''
        # initialize holding the current max area
        max_area = 0
        
        # initialize a pointer to check through each location in the list
        fwd = 0
        # initialize a pointer to start at the end of the list 
        back = len(height)-1
        while fwd != back:
            # for each iteration of the pointers,
            # determine which pointer has a lower height
            side_height = min(height[fwd],height[back]) 
            # determine the distance between the pointers
            distance = back - fwd
            # area = lower height * distance btn
            area = distance*side_height
            # compare to current max 
            max_area = max(max_area, area)
            # (replace if larger)
            
            # compare the height's at each pointer, moving the lower height pointer, if they are the same move the forward moving pointer
            if height[back] >= height[fwd]:
                fwd += 1
            else:
                back -= 1 
        # return max area
        return max_area
        
# remove the nth node from the end of singly-linked list
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Take in a linked list, and an integer with a valid nth node
        
        Removes the nth node, adn returns the head of the linked list
        
        edge case:
        the nth node from the end is the head
        '''
         # two pass solution
        
        LList = head
        # hold a counter for ther length of the LList
        length = 0
        
        # walk through LList to determine length of LList
        while LList:
            length += 1
            LList = LList.next

        LList = head
        # walk through LList and remove the (len(LList) - n + 1)th node
        remove_at = length - n 
        while LList:
            if remove_at == 1:
                node_to_remove = LList.next
                LList.next = node_to_remove.next
                return head
            elif remove_at == 0: # edge case of removing the head
                return LList.next
            remove_at -= 1 
            LList = LList.next

        # One Pass solution
        
        # use a fast and delayed pointer
        # start both at the head
        fast_llist = head
        delayed_llist = head
        # use a counter to record where fast_llist is
        distance = 0
        # move through the LList with the fast pointer
        while fast_llist.next:
            fast_llist = fast_llist.next 
            # only start moving the delayed pointer once fast pointer is n away
            if distance >= n: 
                delayed_llist = delayed_llist.next 
            distance += 1 
        # once fast pointer is None, remove the next node from the slow pointer
        if distance >= n:
            node_to_remove = delayed_llist.next 
            delayed_llist.next = node_to_remove.next
            return head
        else: # edge case of removing the head
            return head.next
            
# Number of unique paths to the end of a board 
# (upon reflection this is similar to the paths to dest prob)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        take in coordinates of the final location (m,n)
        return the number of unique paths from the 'start' (1,1)
        
        m - width
        n - height
        
        assumptions:
        - only positive movement
        - right or down at any one time
        
        example:
        m = 4
        n = 3
        
        1. Right (2,1) > Right (3,1) > Right (4,1) > Down (4,2) > Down (4,3)
        2. R (2,1) > R (3,1) > D (3,2) > R (4,2) > D (4,3)
        3. R (2,1) > R (3,1) > D (3,2) > D (3,3) > D (4,3)
        4. R (2,1) > D (2,2) > D (2,3) > R (3,3) > R (4,3)
        5. R (2,1) > D (2,2) > R (3,2) > R (4,2) > D (4,3)
        6. R (2,1) > D (2,2) > R (3,2) > D (4,2) > R (4,3)
        
        7. D (1,2) > D (1,3) > R (3x) > R > R
        8. D (1,2) > R (2,3) > R (1x) > D (2x) > D
        9. D (1,2) > R (2,3) > D (2x) > D > R (1x) 
        10. D (1,2) > R (2,3) > D (1x) > R (1x) > D (1x)

        (10 options)
        
        1 choice of two options
        limited by dimension
        
        '''
        # Recursive soln: 
        # t = O(2^max(m,n)) 2 calls for all routes larger than m or n == 1
        # space = O(max(m,n)) ~n return statements
        # check if at the edge of the board (x = m or y = n)
        # if at an edge only consider one way to move
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
        
        # Iterative soln:
        # t = O(m*n) + O(n) + O(m) + O(m*n) ~ O(m*n)
        # space = O(m*n)
        
        # make a nested array of 0s on the board of m x n 
        # O(n*m)
        board = [[0 for m_idx in range(m)] for n_idx in range(n)]
        
        # Replace the edges of board with 1 (path from the edge to finish)
        # O(n) + O(m)
        for idx in range(m): # O(m)
            board[n-1][idx] = 1
        for idx in range(n): # O(n)
            board[idx][m-1] = 1
            
        # move through the board and find the number of 
        # paths to each location (from the edge)
        for y in range(n-2,-1,-1): # O(n)
            for x in range(m-2,-1,-1): # O(m)
                board[y][x] = board[y+1][x] + board[y][x+1]
                
        # return the first location on the board 
        # (max number of paths to the end)
        return board[0][0]

# Review Hashmaps and Troubleshoot file readings
# Given  names and phone numbers, assemble a phone book that maps friends
#  names to their respective phone numbers. You will then be given an unknown 
#  number of names to query your phone book for. For each  queried, print the 
#  associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for  is not found, print Not found instead.

phone_book = {}

def check_phone_book(query):
    result = phone_book.get(query)
    if result:
        return query+'='+result
    else:
        return 'Not found'

if __name__ == '__main__':
    entries = int(input())
    for entry in range(0,entries):
        listing = str(input()).split(" ")
        phone_book[listing[0]]=listing[1]
    while True:
        try:
            check = str(input())
            print(check_phone_book(check))
        except EOFError:
            break
            
            
# Recursion (and factorials)
# Recursive Solution: t=O(n) space=O(n)
# makes n+1 calls for all n greater than 1
# the nested calls take up n+1 space
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Find the number of consecutive ones from a number in binary (base two)
# from  a posititive integer in base 10

import math
import os
import random
import re
import sys

def find_max_consecutive_ones_in_binary(n):
    '''takes in a positive integer (n) and returns the
        highest number of consecutive 1's in 
        it's binary form
        
        solution - 
        while loop requires t: O(log(n))
        looping over the binary number is t: O(len(binary_rev))

        but its likely O(log(n)) will be the greater of the two
        time uses in this problem space
        '''
    binary_rev = []
    #translate the number into binary
        # (2^n * 0 or 1)+(2^(n-1) * 0 or 1)
    while n >= 1:
        # hold the remainder of dividing by 2 (0 or 1)
        binary_rev.append(n % 2)
        # loop by dividing n by 2 holding the floor of the result
        n = math.floor(n / 2)    
    # now have the reverse of n in binary
    max_ones = 0
    current_ones = 0
    #loop over the reverse of the number in binary
    for digit in binary_rev:
        # count consectuative number of ones
        if digit == 1:
            current_ones += 1
            # replace a max consecutive number when surpassed
            if current_ones > max_ones:
                max_ones = current_ones
        # restart when a zero is encountered
        else:
            current_ones = 0
    return max_ones    

if __name__ == '__main__':
    n = int(input())
    print(find_max_consecutive_ones_in_binary(n))

# inheritance practice
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores=[]):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        '''Assume at least one score is available'''
        average = scores[0]
        for idx in range(1,len(scores)):
            average = (average + scores[idx])/2
        if average >= 90:
            return 'O'
        elif average >= 80:
            return 'E'
        elif average >= 70:
            return 'A'
        elif average >= 55:
            return 'P'
        elif average >= 40:
            return 'D'
        else:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

# Abstract class practice
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price=price
    def display(self):
        print('Title: '+str(self.title))
        print('Author: '+str(self.author))
        print('Price: '+str(self.price))
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()


## Practice with scope and finding the largest difference in a list of numbers
# O(n logn) solution
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        # sort the elements O(nlogn)
        sorted_elements = sorted(self.__elements)
        largest = sorted_elements[-1]
        smallest = sorted_elements[0]
        self.maximumDifference = abs(largest-smallest)

# O(n) solution
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        smallest = self.__elements[0]
        largest = self.__elements[0]
        for idx in range(1,len(self.__elements)):
            if self.__elements[idx] > largest:
                largest = self.__elements[idx]
            if self.__elements[idx] < smallest:
                smallest = self.__elements[idx]
        self.maximumDifference = abs(largest - smallest)


#testing
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# LList formulation practice

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data):
        if not head:
            head = Node(data)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(data)
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 


# Two Exception Throwing / Handling Practice problems
# Exception Handling
S = input().strip()
try:
    intS = int(S)
    print(intS)
except:
    print('Bad String')
# Exception Throwing
class Calculator:
    def __init__(self):
        pass
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        else:
            return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 
        
## A naive palindrome checker useing two arrays as a stack and queue
class Solution:
    def __init__(self,stack=[],queue=[]):
        self.stack = stack
        self.queue = queue
    def pushCharacter(self, char):
        self.stack.append(char)
    def enqueueCharacter(self,char):
        self.queue.append(char)
    def popCharacter(self):
        return self.stack.pop(-1)
    def dequeueCharacter(self):
        return self.queue.pop(0)
        
 read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 
    
# Bubble Sort Implementation
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
def bubbleSort(a):
    num_swaps = 0
    # ensures all elements get len(a) oppertunities to swap (if worst case list is reversed)
    for idx in range(len(a)-1): 
        # goes through each element and compares to following element
        for idx in range(len(a)-1):
            # swaps if next element is smaller 
            if a[idx] > a[idx+1]:
                a[idx], a[idx+1] = a[idx+1], a[idx]
                num_swaps+=1    
    return a, num_swaps

sorted_a, swaps = bubbleSort(a)
print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(sorted_a[0]))
print('Last Element: {}'.format(sorted_a[-1]))

# Naive get longest height of BST
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        # if both paths exist, return the max path length of the two
        if root.left and root.right:
            return max(self.getHeight(root.left),self.getHeight(root.right)) + 1 
        # if only one path exists follow it down
        elif root.left:
            return self.getHeight(root.left) + 1
        elif root.right:
            return self.getHeight(root.right) + 1
        # if they do not return zero as the height from both
        else:
            return 0

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)   

# Breadth First Search of a Binary Search Tree
mport sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        '''Traverses the BST using BFS
            Will implement a queue using an array but collections.duque 
            or queue.Queue would likely be better objects (constant time look up)
            Assume no duplicate values exist in the tree
        '''
        # form an array to hold the order of the nodes visited
        visited = []
        # form a queue f nodes to look at (starting with the root)
        queue = [root]
        # while there is anything in the queue, loop through it
        while queue:
            # start by popping off the first item of the queue
            current = queue.pop(0)
            # add it's value to the visited array as a string
            visited.append(str(current.data))
            # check if it has anything in it's left or right nodes
            # if anything in left, add it to the end of the queue
            if current.left:
                queue.append(current.left)
            # if anything in right, add it to the end of the queue
            if current.right:
                queue.append(current.right)
        # join the visited elements with spaces and return the string
        print(' '.join(visited))
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

## 
## Merge k sorted linked lists and 
## return it as one sorted list. Analyze and describe its complexity.
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        Merged a list of k llists into one sorted llist
        
        Assume:
        - no duplicate values in any one llist
        - assume no empty inputs
        - all elements are integers
        '''
        
        if len(lists) == 0:
            return None
        
        ## ~ O(n^2)
        # sorted_values = []
        # # loop through each linked list
        # for llist in lists: # n^2
        #     while llist: 
        #         sorted_values.append(llist.val)
        #         llist = llist.next 
        # # resort the elements in the array
        # sorted_values.sort() # n logn
        # # move items in the array to result in one sorted array
        # first_item = sorted_values.pop(0)
        # merged_llist = ListNode(first_item)
        # print(merged_llist.val)
        # head = merged_llist
        # for ele in sorted_values: # n
        #     merged_llist.next = ListNode(ele)
        #     merged_llist = merged_llist.next
        # return head
        
        # maybe better:
        # start with an empty llist
        head = None
        
        # loop through the arr of llist:
        while lists:
            # hold current items
            new_elements = deque()
            # at each node, take the current value of every llist
            for idx in range(len(lists)): # O(n)
                if lists[idx]:
                    new_elements.append(lists[idx].val)
                    lists[idx] = lists[idx].next
                # else:
                #     lists.pop(idx)
            # if new_elements is empty, there are no nodes to add
            if len(new_elements) == 0:
                break
            # add each item into a llist in correct spot
            if not head:
                head = ListNode(new_elements.popleft())
            while new_elements: # O(k)
                current = new_elements.popleft()
                # traverse llist and compare each node's val
                # to the current element
                # if the the element is smaller than the head
                if current <= head.val:
                    hold = head.val
                    head = ListNode(current, ListNode(hold, head.next))
                # otherwise go through and compare the new ele
                # to the next node
                else:
                    pointer = head
                    while True:
                        # if there is a value to compare to 
                        if pointer.next:
                        # move the next node down and insert the current value if smaller
                            if current <= pointer.next.val:
                                hold = pointer.next
                                pointer.next = ListNode(current, hold)
                                break
                        # otherwise keep looking
                            else:
                                pointer = pointer.next
                        # if there isn't a next, append to end of llist
                        else:
                            pointer.next = ListNode(current) 
                            break
        return head
        
## Remove duplicates from a llist in-place

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        '''The is assumed to have no order
        '''
        seen = set()
        pointer = head
        seen.add(head.data)
        while head.next:
            next_node = head.next
            if next_node.data in seen:
                head.next = next_node.next
            else:
                seen.add(next_node.data)
                head = head.next
        return pointer

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

# Check if Prime Optimal Solution
import math

def check_if_prime(n):
    '''Determines if the input integer is prime
    
       A prime number is 
       - a number greater than one
       - that is only divisible by 1 and itself    
    '''
    # handle edge case of less than one
    if n <= 1:
        return 'Not prime'

    # utilize square roots and primes
    # sqrt(n)*sqrt(n)=n and to check if prime we are checking for 
    # divisible factors such that
    # n = a*b. as such a,b < n 
    # with this we only need to check for
    # divisible factors between 1 & sqrt(n) 

    # this enables a O(sqrt(n)) solution
    for num in range(2,math.floor(math.sqrt(n))+1):
        if n % num == 0:
            return 'Not prime'
    return 'Prime'

N=int(input())
head=None
for i in range(N):
    n=int(input())
    print(check_if_prime(n))
