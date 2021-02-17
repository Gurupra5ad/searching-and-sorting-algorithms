""" Take a list of sorted numbers (i.e., descending or ascending order) 
and perform a search on that list for the element that had to be found by the user.
The basic ideas is to find the mid number of the array,
 check the element with that number if that matches great, 
 or else check whether the number is greater or lesser than the mid num
and perform the search accordingly on the required half of the array """

def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1

n = int(input("enter the number of elements in the array"))
arr =[]
for i in range(n):
    arr.append(int(input("Enter the element of the list")))

x = int(input("Enter the element that need to be found"))
  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present") 
else: 
    print ("Element is not present in array") 
