""" Jump Search is a searching algorithm for sorted arrays. 
The basic idea is to check fewer elements (than linear search) by jumping 
ahead by fixed steps or skipping some elements in place of searching all elements. """

import math 
  
def jump_search( arr , x , n ): 
      
    # Finding block size to be jumped 
    step = math.sqrt(n) 
      
    # Finding the block where element is 
    # present (if it is present) 
    prev = 0
    while arr[int(min(step, n)-1)] < x: 
        prev = step 
        step += math.sqrt(n) 
        if prev >= n: 
            return -1
      
    # Doing a linear search for x in  
    # block beginning with prev. 
    while arr[int(prev)] < x: 
        prev += 1
          
        # If we reached next block or end  
        # of array, element is not present. 
        if prev == min(step, n): 
            return -1
      
    # If element is found 
    if arr[int(prev)] == x: 
        return prev 
      
    return -1

n = int(input("enter the number of elements in the array"))
arr =[]
for i in range(n):
    arr.append(int(input("Enter the element of the list")))

x = int(input("Enter the element that need to be found"))
  
result = jump_search(arr,x,n) 
  
if result != -1: 
    print ("Element is present") 
else: 
    print ("Element is not present in array") 
