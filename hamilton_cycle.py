def find_hamilton_cycles(graph):
    n = len(graph)
    hamiltonCycles = []

    def dfs(start,node,visited,path):
        nonlocal hamiltonCycles

        if len(path) == n and start in graph[node]:
            path.append(start)
            hamiltonCycles.append(path[:])
            return
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(start, neighbor, visited, path + [neighbor])
                visited.discard(neighbor)  


    dfs(0, 0, {0}, [0])
    
    return hamiltonCycles

# graph = {}
# graph[0] = set([1,3])
# graph[1] = set([0,2,3,4])
# graph[2] = set([1,4])
# graph[3] = set([0,1,4])
# graph[4] = set([1,2,3])

# Leetcode: 

graph = {}
graph[0] = set([1,2,5])
graph[1] = set([0,2,4,5])
graph[2] = set([0,1,3])
graph[3] = set([2,4])
graph[4] = set([1,3,5])
graph[5] = set([0,1,4])

print(find_hamilton_cycles(graph))