
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

# Graph = {
#     0: {
#         1: 3,
#         4: 5
#     },
#     1: {
#         ...
#     }
# }

# 0 has 2 neighbors, 1 and 4, with weights 3 and 5 respectively

from queue import PriorityQueue
def prims(graph, n):
    mstSet = set()
    pq = PriorityQueue()
    pq.put((0, 0, 0))
    mst = []

    while len(mst) < n and not pq.empty():
        weight, node, parent = pq.get()
        if node not in mstSet:
            mstSet.add(node)
            mst.append([weight, parent, node])
            for neighbor in graph[node]:
                if neighbor not in mstSet:
                    pq.put((graph[node][neighbor], neighbor, node))
    mst.sort()
    return mst[1:]

graph = {6: {7: 1, 5: 2, 8: 6}, 7: {6: 1, 8: 7, 0: 8, 1: 11}, 2: {8: 2, 5: 4, 3: 7, 1: 8}, 8: {2: 2, 6: 6, 7: 7}, 5: {6: 2, 2: 4, 4: 10, 3: 14}, 0: {1: 4, 7: 8}, 1: {0: 4, 2: 8, 7: 11}, 3: {2: 7, 4: 9, 5: 14}, 4: {3: 9, 5: 10}}

# Note: the graph and edges in both the examples represent the same graph but will yield different answers as one graph can have multiple MSTs
print(prims(graph, 9))
