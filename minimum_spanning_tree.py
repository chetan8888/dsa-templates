# Leetcode Questions: https://leetcode.com/tag/minimum-spanning-tree/

# edges => 3:[[0,1],[3,2]] 5:[[1,2]] there are three edges, two of weight 3 between 0,1 and 2,3 and one of 5 between 1,2
# returns an array [[a,b,c],[d,e,f]] where a is edge weight between b,c

# Kruskal's algorithm
# 1. Sort all the edges in non-decreasing order of their weight.
# 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
#    If cycle is not formed, include this edge. Else, discard it.
# 3. Repeat step#2 until there are (V-1) edges in the spanning tree.

def find_parent(x,parent):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x],parent)
    return parent[x]

def union(a,b,rank,parent):
    parent_a = find_parent(a,parent)
    parent_b = find_parent(b,parent)

    if parent_a != parent_b:
        if rank[parent_a] < rank[parent_b]:
            parent[parent_a] = parent_b
        elif rank[parent_a] > rank[parent_b]:
            parent[parent_b] = parent_a
        else:
            parent[parent_b] = parent_a
            rank[parent_a] += 1

def find_mst(edges,n):
    mst = []
    weights = []
    for k in edges:
        weights.append(k)
    weights.sort()

    rank = [0 for i in range(n)]
    parent = [i for i in range(n)]

    for weight in weights:
        for a,b in edges[weight]:
            if find_parent(a,parent) != find_parent(b,parent):
                union(a,b,rank,parent)
                mst.append([weight,a,b])
    # A Spanning Tree with n vertices will always have n-1 edges.
    if len(mst) != n-1:
        print("Graph is not connected")
    return mst

edges = {}
edges[1] = [[6,7]]
edges[2] = [[2,8],[6,5]]
edges[4] = [[0,1],[2,5]]
edges[6] = [[8,6]]
edges[7] = [[2,3],[7,8]]
edges[8] = [[0,7],[1,2]]
edges[9] = [[3,4]]
edges[10] = [[5,4]]
edges[11] = [[1,7]]
edges[14] = [[3,5]]
print(find_mst(edges,9))



# Prim's algorithm
# 1. Create a set mstSet that keeps track of vertices already included in MST.
# 2. Start with any vertex and add it to mstSet. Also, add all edges from this vertex to a priority queue.
# 3. Keep picking edges from priority queue and if the edge picked is not in mstSet, add it to mstSet and add all its adjacent edges to the priority queue.
# 4. Repeat step#3 until there are (V-1) edges in the spanning tree.

# graph = {
#     1: [(3,2),(5,3)],
#     2: [(3,1),(1,3),(6,4),(5,5)],
# }
# 1 has 2 neighbors, 2 and 3, with weights 3 and 5 respectively

from heapq import heappop, heappush
def prims(graph, n):
    totalCost = 0

    mst = []
    visited = set()

    h = [(0,0,0)]

    while h and len(visited) < n:
        weight, vertex, parent = heappop(h)
        if vertex not in visited:
            totalCost += weight
            visited.add(vertex)
            mst.append([weight, parent, vertex])
            for nw, neighbor in graph[vertex]:
                if neighbor not in visited:
                    heappush(h, (nw, neighbor, vertex))
    mst = mst[1:]
    if len(mst) != n-1:
        print("Graph is not connected")
    mst.sort()
    return mst

graph = {0: [[4, 1], [8, 7]], 1: [[4, 0], [8, 2], [11, 7]], 2: [[2, 8], [4, 5], [7, 3], [8, 1]], 3: [[7, 2], [9, 4], [14, 5]], 4: [[9, 3], [10, 5]], 5: [[2, 6], [4, 2], [10, 4], [14, 3]], 6: [[1, 7], [2, 5], [6, 8]], 7: [[1, 6], [7, 8], [8, 0], [11, 1]], 8: [[2, 2], [6, 6], [7, 7]]}

print(prims(graph,9))



