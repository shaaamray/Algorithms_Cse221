import heapq
file_input = open('input4.txt','r')
file_output = open('output4.txt', 'w')

def Network(Graph, source):
    dist = []
    for i in range(len(Graph)+1):
        dist.append(-7777777)
    dist[source] = 0
    
    Q = []
    visited = []
    for i in range(len(Graph)+1):
        visited.append(0)
        
    prev = []
    for i in range(len(Graph)+1):
        prev.append(0)
    prev[source] = 1
    
    for v in Graph:
        heapq.heappush(Q, (dist[v], v))
        
    heapq._heapify_max(Q)
        
    while len(Q) != 0:
        u, l = heapq._heappop_max(Q)
        
        if visited[l] == 1:
            continue
        
        visited[l] = 1
        for v in Graph[l]:
            alt = 0
            
            if u == 0:
                alt = v[1]
            elif v[1] == 0:
                alt = u
            elif u < v[1]:
                alt = u
            else:
                alt = v[1]
                
            if alt > dist[v[0]]:
                dist[v[0]] = alt
                prev[v[0]] = l
                heapq.heappush(Q, (dist[v[0]], v[0]))
                heapq._heapify_max(Q)
                
    return dist
a = {}
val = list()
for i in file_input:
    val.append(i)
    
for j, k in enumerate(val):
    val[j] = k.replace('\n','')

val = val[1:]
arr = []    
for j in val:
    store = j.split()
    arr.append(store)

b = 0
add_val = 1
while b < len(arr):
    arr2 = arr[b]
    if len(arr2) == 2:
        case1 = int(arr2[0])
        case2 = int(arr2[1])
        
    if len(arr2) == 3 or len(arr2) == 1:
        b += 1
    elif case1 == 1:
        a[case1] = []
        temp = int(arr[b+1][0])
        dist = Network(a, temp)
        file_output.write("0\n")
        b += 1
        a = {}
    elif case1 > 1:
        c = b + 1
        add_val2 = 1
        temp = 0
        
        for i in range(case2):
            if add_val2 == case2:
                way1 = int(arr[c][0])
                way2 = int(arr[c][1])
                traffic = int(arr[c][2])
                temp = int(arr[b + case2 + 1][0])
                
                if way1 not in a:
                    a[way1] = []
                
                if way2 not in a:
                    a[way2] = []
                    
                a[way1].append([way2, traffic])
                c += 1
            else:
                way1 = int(arr[c][0])
                way2 = int(arr[c][1])
                traffic = int(arr[c][2])
                add_val2 += 1
                
                if way1 not in a:
                    a[way1] = []
                
                if way2 not in a:
                    a[way2] = []
                    
                a[way1].append([way2, traffic])
                c += 1
                
        dist = Network(a, temp)
        dist = dist[1:]
        result = ""
        for j in dist:
            if j < -1:
                result += str(-1)+" "
            else:
                result += str(j)+" "
        
        file_output.write(result+"\n")
                         
        b += 1
        add_val += 1
    a = {}
file_input.close()
file_output.close()