""" Bubble Sort is the simplest sorting algorithm that works by 
repeatedly swapping the adjacent elements if they are in wrong order """

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(int(arr[i]) > int(arr[j])):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

n = int(input("enter the number of elements in the array"))
arr =[]
for i in range(n):
    arr.append(int(input("Enter the element of the list")))

print(bubble_sort(arr))   
    