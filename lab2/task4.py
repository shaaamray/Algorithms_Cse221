file_input = open("input4.txt", "r")
file_output = open("output4.txt", "w")
arr1 = []
for i in file_input:
    arr1.append(i)
data_list = arr1[1].split(" ")
for i in range(len(data_list)):
    data_list[i] = int(data_list[i])

def mergeSort(num):
    arr2 = []
    if len(num) < 2:
        return num
    mid = int(len(num)/2)
    a = mergeSort(num[:mid])
    b = mergeSort(num[mid:])
    while (len(a) > 0) or (len(b) > 0):
        if len(a) > 0 and len(b) > 0:
            if a[0] > b[0]:
                arr2.append(b[0])
                b.pop(0)
            else:
                arr2.append(a[0])
                a.pop(0)
        elif len(b) > 0:
            for i in b:
                arr2.append(i)
                b.pop(0)
        else:
            for i in a:
                arr2.append(i)
                a.pop(0)
    return arr2


n = mergeSort(data_list)
for i in n:
    file_output.write(str(i)+" ")

file_input.close()
file_output.close()