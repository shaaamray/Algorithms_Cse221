'''Time complexity of bubble sort in case of best case scenario is 0(n), 
if we consider a sorted array for the function and in that case it will use
only one loop '''
file_input = open("input1.txt", "r")
file_output = open("output1.txt", "w")
arr1 = []
for i in file_input:
    arr1.append(i)

element = arr1[1].split(" ")

def bubbleSort(arr):
    i = 0
    while i <= len(arr)-1:
        swap = False
        i += 1
        
        j = 0
        while j <= len(arr)-i-1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            j += 1
        if swap == False:
            break
    return arr
final_sort = bubbleSort(element)
for i in final_sort:
    file_output.write(i+" ")
    
file_input.close()
file_output.close()
        