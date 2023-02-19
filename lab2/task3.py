file_input = open("input3.txt", "r")
file_output = open("output3.txt", "w")
arr1 = []

for i in file_input:
    arr1.append(i)
    
total_student = int(arr1[0].replace("\n", ""))
id_num = arr1[1].replace("\n", "")
marks_num = arr1[2].replace("\n", "")
id_num = id_num.split(" ")
marks_num = marks_num.split(" ")

arr2 = []
for i in marks_num:
    arr2.append(int(i))

def insertionSort(n, id_num):
    for i in range(len(n)-1):
        pre = n[i+1]
        post = id_num[i+1]
        j = i
        while 0 <= j:
            if n[j] < pre:
                n[j+1] = n[j]
                id_num[j+1] = id_num[j]
            else:
                break
            j -= 1
        n[j+1] = pre
        id_num[j+1] = post
    return id_num

final_sort = insertionSort(marks_num, id_num)
for i in final_sort:
    file_output.write(i+" ")

file_input.close()
file_output.close()