import task1

def DFS_VISIT(graph, node):
    visited[int(node)-1] = 1
    printed.append(node)
    
    for each_node in graph[node]:
        if each_node not in visited:
            DFS_VISIT(graph, each_node)
            
    return printed

def DFS(graph, endPoint):
    file_output = open('output3.txt','w')
    file_output.write("Places: ")
    arr2 = []
    
    for node in graph:
        if node not in visited:
            arr2 = DFS_VISIT(graph, node)
    for i in range(0, len(arr2)):
        if str(arr2[i]) == endPoint:
            file_output.write(str(arr2[i])+" ")
            break
        else:
            file_output.write(str(arr2[i])+" ")
    file_output.close()
visited = [0] * task1.count
printed = []
DFS(task1.map, '12')