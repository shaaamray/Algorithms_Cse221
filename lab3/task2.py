import task1

def BFS(visit, graph, node, endPoint):
    file_output = open('output2.txt','w')
    arr1 = []
    visit[int(node)-1] = 1
    arr1.append(node)
    span = len(arr1)
    file_output.write("Places: ")
    
    while span != 0:
        m = arr1.pop(0)
        file_output.write(str(m)+" ")
        
        if int(m) == int(endPoint):
            break
        for node in graph[int(m)]:
            if not visit[int(node)-1]:
                visit[int(node)-1] = 1
                arr1.append(node)
        
    file_output.close()
                
visited = [0]*task1.count
BFS(visited, task1.map, '1', '12')
                