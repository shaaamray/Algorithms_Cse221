file_input = open('task3_input.txt', 'r')
file_output = open('task3_output.txt', 'w')

array_1 = []
for j in file_input.readlines():
    array_1.append(j)

array_2 = []
for j in array_1:
    val = j.replace('\n','')
    array_2.append(val)

a = int(array_2[0])
activity = array_2[1].split()
p = array_2[2]

for j in range(len(activity)):
    key = j
    for k in range(j+1,len(activity)):
        if int(activity[key]) > int(activity[k]):
            key = k
    activity[j], activity[key] = activity[key], activity[j]

result = []

Jack = []
Jill = []

jack_timing = 0
jill_timing = 0
c = 0
for j in p:
    if j == 'J':
        jack_act = activity[c]
        Jack.append(jack_act)
        jack_timing += int(jack_act)
        result.append(jack_act)
        c += 1
    else:
        num = 0
        val = Jack
        final_time = val.pop()
        check = True
        
        while check:
            if final_time not in Jill:
                Jill.append(final_time)
                jill_timing += int(final_time)
                result.append(final_time)
                check = False
            else:
                num += 1
                final_time = val[num]

for j in result:
    file_output.write(j)

file_output.write('\n')
file_output.write('Jack will work for '+str(jack_timing)+" hours\n")
file_output.write('Jill will work for '+str(jill_timing)+" hours\n")

file_input.close()
file_output.close()