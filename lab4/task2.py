import heapq
file_input = open("input1.txt", 'r')
file_output = open("output2.txt", 'w')

def Dijkstra(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(7777777)
    dist[source] = 0
    Q = []
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
    prev = []
    for i in range(len(Graph)+1):
        prev.append(0)
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))
    while len(Q) != 0:
        u, l = heapq.heappop(Q)
        if visited[l]:
            continue
        visited[l] = True
        
        for v in Graph[l]:
            alt = u + v[1]
            if alt < dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = l
                heapq.heappush(Q, (dist[v[0]], v[0]))
    return prev

a = {}
val = list()

for i in file_input:
    val.append(i)
for i, j in enumerate(val):
    val[i] = j.replace('\n','')

val = val[1:]
arr = []
b = 0
for i in val:
    store = i.split()
    arr.append(store)
for j in arr:
    if len(j) == 3:
        continue
    if len(j) == 2:
        case1 = int(j[0])
        case2 = int(j[1])
        if case1 == 1:
            b += 1
            a[case1] = []
            
            idealWay = Dijkstra(a, 1)
            idealWay = idealWay[1:]
            for z in idealWay:
                if z == 0:
                    file_output.write("1\n")
        else:
            b +=1
            for k in range(case2):
                way1 = int(arr[b][0])
                way2 = int(arr[b][1])
                traffic = int(arr[b][2])
                if way1 not in a:
                    a[way1] = []
                if way2 not in a:
                    a[way2] = []
                a[way1].append([way2, traffic])
                b +=1
            idealWay = Dijkstra(a, 1)
            c = ""
            arr2 = []
            arr2.append(len(a))
            num = len(a)
            while num != 1:
                arr2.append(idealWay[num])
                num = idealWay[num]
            arr2.reverse()
            for j in arr2:
                c += str(j)+" "
            file_output.write(c+"\n")
            a = {}

file_input.close()
file_output.close()
    
    