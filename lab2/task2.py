file_input = open("input2.txt", "r")
file_output = open("output2.txt", "w")
arr1 = []
for i in file_input:
    arr1.append(i)
num = arr1[0].split(" ")
repeater = int(num[1].replace("\n",""))
num = arr1[1].split(" ")

def selectionSort(arr2):
    span = len(arr2)
    for i in range(span):
        n = i
        for j in range(i+1, span):
            if int(arr2[n]) > int(arr2[j]):
                n = j
        store = arr2[i]
        arr2[i] = arr2[n]
        arr2[n] = store
    return arr2
final_sort = selectionSort(num)
for i in range(repeater):
    file_output.write(str(final_sort[i])+" ")

file_input.close()
file_output.close()