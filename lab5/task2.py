file_input = open("task2_input.txt",'r')
file_output = open("task2_output.txt", 'w')

array_1 = []

for j in file_input.readlines():
    array_1.append(j)

array_2 = []
for j in array_1:
    val = j.replace('\n','')
    array_2.append(val)

list = array_2.pop(0)
activity, people = list.split()
activity = int(activity)
people = int(people)

last_array = []
for j in array_2:
    last_array.append(j.split())

c = 1
for j in range(int(activity)):
    key = j
    for k in range(j+1,int(activity)):
        if int(last_array[key][c]) > int(last_array[k][c]):
            key = k
    last_array[j], last_array[key] = last_array[key], last_array[j]
    
count = 0
new_array = []
for j in range(people):
    new_array.append(0)

b = 0
for j in range(people):
    count += 1
    val = last_array.pop(0)
    new_array[b] = val[1]
    b += 1
for j in last_array:
    start = int(j[0])
    finish = int(j[1])
    for k in range(len(new_array)):
        if int(new_array[k]) <= start:
            count += 1
            new_array[k] = finish
            break
file_output.write(str(count)+'\n')
file_input.close()
file_output.close()

        