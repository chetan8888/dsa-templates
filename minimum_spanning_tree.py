
# edges => 3:[[0,1],[3,2]] 5:[[1,2]] there are three edges, two of weight 3 between 0,1 and 2,3 and one of 5 between 1,2
# returns an array [[a,b,c],[d,e,f]] where a is edge weight between b,c

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
        for pair in edges[weight]:
            if find_parent(pair[0],parent) != find_parent(pair[1],parent):
                union(pair[0],pair[1],rank,parent)
                mst.append([weight,pair[0],pair[1]])
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