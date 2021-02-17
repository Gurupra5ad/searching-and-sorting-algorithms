""" Take input of list of elements and the element need to be
 found by the user and run a search sequuentially in the 
 list of elements"""

def linear_search(usr_lst, elem):
    for item in usr_lst:
        if elem==item:
            return "Element found"
    
    return " Element not found"

usr_lst = input("Enter values comma seperated").split(",")
elem = input("Enter the element that needs to be found")

print(linear_search(usr_lst, elem))