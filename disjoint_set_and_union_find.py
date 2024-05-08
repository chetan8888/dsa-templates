# Always think about disjoint sets in graph questions

def find(parent,x):
    if parent[x] == x:
        return x
    # for Path compression reassign the parent returne by downstream find call
    # parent[x] = find(parent[x])
    return find(parent,parent[x])

def union(parent,a,b):
    parent_a = find(parent,a)
    parent_b = find(parent,b)

    if parent_a != parent_b:
        parent[b] = parent_a

def union_by_rank(rank,parent,a,b):
    parent_a = find(parent,a)
    parent_b = find(parent,b)

    if parent_a != parent_b:
        if rank[parent_a] < rank[parent_b]:
            parent[parent_a] = parent_b
        elif rank[parent_a] > rank[parent_b]:
            parent[parent_b] = parent_a
        else:
            parent[parent_b] = parent_a
            rank[parent_a] += 1

def find_pathcompression(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find_pathcompression(parent,parent[x])
    return parent[x]



a = [0,1,2,3,4]
parent = [i for i in range(len(a))]
rank = [0 for i in range(len(a))]

# union(parent,0,1)
# print(find(parent,0))
# print(find(parent,1))

# union_by_rank(rank,parent,0,1)
# print(find_pathcompression(parent,1))
# union_by_rank(rank,parent,1,2)
# print(find_pathcompression(parent,2))
