# Articulation point is a node in a graph that if removed, the graph will be disconnected
# This algorithm is based on the DFS tree of the graph
# The DFS tree is a tree that is formed by DFS traversal of the graph

# The algorithm is as follows:
# 1. Do a DFS traversal of the graph
# 2. For each node, keep track of the order in which it is visited
# 3. For each node, keep track of the lowest reachable node from that node
# 4. For each node, keep track of the children of that node
# 2 conditions for articulation point:
    # a) If the root has at least two children, then the root is an articulation point
    # b) For each non root node, if one of its children has no back edge to any of its ancestor, then that node is an articulation point

# References: https://www.youtube.com/watch?v=jFZsDDB0-vo
# https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/

from math import inf

def articulationPoint(graph):
    n = len(graph)
    dfsVisitOrder = [inf for node in range(n)]
    lowestReachable = [inf for node in range(n)]
    visited = [False for node in range(n)]
    orderNum = 0
    articulationPoints = set()
    rootChildren = 0

    def dfs(node):
        nonlocal orderNum, rootChildren
        
        dfsVisitOrder[node] = orderNum
        orderNum += 1
        visited[node] = True
        minReachable = dfsVisitOrder[node]

        for neighbor in graph[node]:
            minReachable = min(minReachable, dfsVisitOrder[neighbor])
            if not visited[neighbor]:                
                currMinReachable = dfs(neighbor)
                minReachable = min(minReachable, currMinReachable)

                # Root Node Articulation Point Check
                if node == 0:
                    rootChildren += 1
                # Non Root Node Articulation Point Check
                else:
                    # For each node, if one of its children has no back edge to any of its ancestor, then that node is an articulation point
                    if lowestReachable[neighbor] >= dfsVisitOrder[node]:
                        articulationPoints.add(node)

        lowestReachable[node] = minReachable
        return lowestReachable[node]

    dfs(0)
    if rootChildren >= 2:
        articulationPoints.add(0)
    return articulationPoints

graph = {}
graph[0] = [1, 2]
graph[1] = [0, 2, 3, 4, 6]
graph[2] = [0, 1]
graph[3] = [1, 5]
graph[4] = [1, 5]
graph[5] = [3, 4]
graph[6] = [1]
print(articulationPoint(graph))

graph = {}
graph[0] = [1, 3]
graph[1] = [0, 2]
graph[2] = [1, 3, 4, 5]
graph[3] = [0, 2]
graph[4] = [2, 5]
graph[5] = [2, 4]
print(articulationPoint(graph))