# https://www.youtube.com/watch?v=eL-KzMXSXXI&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=15&ab_channel=WilliamFiset

topologicalOrdering = []
def dfs(node, graph, visited):
    visited.add(node)

    for neigh in graph[node]:
        if neigh not in visited(dfs(neigh))
    
    topologicalOrdering.append(node)

dfs(any random node)