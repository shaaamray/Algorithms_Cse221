file_input = open("task1_input.txt", "r")
file_output = open("task1_output.txt", "w")
array_1 = []

for j in file_input.readlines():
    array_1.append(j)

array_2 = []
for j in array_1:
    val = j.replace('\n','')
    array_2.append(val)

a = int(array_2.pop(0))

last_array = []
for j in array_2:
    last_array.append(j.split())

c = 1
for j in range(a):
    key = j
    for k in range(j+1,a):
        if int(last_array[key][c]) > int(last_array[k][c]):
            key = k
    last_array[j], last_array[key] = last_array[key], last_array[j]

result = []
result.append(last_array.pop(0))
count = 1

f = result[0][1] 
for j in last_array:
    start = int(j[0])
    finish = int(j[1])
    if int(f) <= start:
        result.append(j)
        count += 1
        f = finish

file_output.write(str(count)+'\n')
for j in result:
    file_output.write(str(j[0])+" "+str(j[1])+'\n')

file_input.close()
file_output.close()