file_input = open('input1.txt','r')
myArr = []
map = {}
for i in file_input:
    myArr.append(i.split())
count = int(myArr[0][0])
myArr = myArr[1:]
for i in myArr:
    place = int(i[0])
    path = i[1:]
    for j, k in enumerate(path):
        path[j] = int(k)
    map[place] = path

file_input.close()