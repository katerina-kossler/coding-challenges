# Document for Organizing Bits of Info While Reviewing & Practicing with others

# Swapping
  '''
  
  hold = obj[idx]
  obj[idx] = obj[new_idx]
  obj[new_idx] = hold
  
  
  item[idx_1], item[idx_2] = item[idx_2], item[idx_1]
  
  '''
# Permutations and Combinations 
  '''
  britanica = various ways in which objects from 
  a set may be selected, generally without replacement, to form subsets.
  
  permutation = order of selection is a factor 
  combination = order is not a factor
  
  ex: 2 elements from ABCD
  
  1) (P)ermutation:
    P = {AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC} > 12
    
  2) (C)ombination:
    C = {AB=BA, AC=CA, AD=DA, BC=CB, BD=DB, CD=DC} > 6
    
  Finding the Number of Possible P/C:
    (r chosen from n elements)
  
  P = n! / ((n-r)!) = (1*2*...*n)/(1*2*...*(n-r))
  
  C = n! / ((n-r)!*(r)!) = (1*2*...*n)/[(1*2*...*(n-r))*(1*2*...*r)]
   
  Determining whether to find a set of P or C:
    P) English words - letter order matters but keep track of dupl. words,
       Giving numbers to players on a 
    C) Fruit from a basket, players from a class
  '''

