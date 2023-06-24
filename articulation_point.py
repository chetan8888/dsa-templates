# Articulation point is a node in a graph that if removed, the graph will be disconnected
# This algorithm is based on the DFS tree of the graph
# The DFS tree is a tree that is formed by DFS traversal of the graph

# The DFS tree has the following properties:
# 2. A node is an articulation point if it is the root of the DFS tree and has at least two children
# 3. A node is an articulation point if it is not the root of the DFS tree and it has a child that has no back edge to any of its ancestor

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
    dfsVisitOrder = [-1 for node in range(n)]
    lowestReachable = [inf for node in range(n)]
    visited = [False for node in range(n)]
    orderNum = 0
    rootHasTwoChildren = False
    articulationPoints = []

    def dfs(node):
        nonlocal orderNum, rootHasTwoChildren
        if node >= n:
            return
        
        dfsVisitOrder[node] = orderNum
        orderNum += 1
        visited[node] = True
        minReachable = node
        children = set()

        for neighbor in graph[node]:
            minReachable = min(minReachable, neighbor)
            if not visited[neighbor]:
                children.add(neighbor)
                minReachable = min(minReachable, dfs(neighbor))
        
        # Root node is an articulation point if it has at least two children
        if node == 0:
            if len(children) >= 2:
                # rootHasTwoChildren = True
                articulationPoints.append(node)
        else:
            # For each node, if one of its children has no back edge to any of its ancestor, then that node is an articulation point
            for child in children:
                if lowestReachable[child] >= dfsVisitOrder[node]:
                    articulationPoints.append(node)
                    break

        lowestReachable[node] = minReachable
        return minReachable

    dfs(0)
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