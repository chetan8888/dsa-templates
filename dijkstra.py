from queue import PriorityQueue
import math

# For DAG use simple BFS to find shortest distance (O(V+E))

# graph => 1:[[0,2],[3,4]]   1 has 2 neighbors 0 and 3 at distances 2 and 4
# Djikstra works only for positive edges. For negative edges use Bellman Ford
# O((V+E)logV)

def find_min_distance(graph,source,target,n):
    dist = [9999999 for i in range(n)]
    pq = PriorityQueue()
    dist[source] = 0
    pq.put((0,source))

    while not pq.empty():
        cn = pq.get()[1]
        for neighbor in graph[cn]:
            if dist[neighbor[0]] > dist[cn] + neighbor[1]:
                dist[neighbor[0]] = dist[cn] + neighbor[1]
                pq.put((dist[neighbor[0]],neighbor[0]))
    return dist[target]

graph = {}
graph[0] = [[1,1],[3,10]]
graph[1] = [[2,2]]
graph[2] = [[3,4]]
graph[3] = []
print(find_min_distance(graph,0,3,4))


# Bellman Ford (O(V*E))
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
# Be careful of negative cycles

def bellmanFord(edges, n, source):
    dist = [math.inf for i in range(n)]
    dist[source] = 0

    for i in range(n-1):
        for u,v,w in edges:
            dist[v] = min(dist[v], dist[u]+w)
    return dist

edges = []
edges.append([0, 1, -1])
edges.append([0, 2, 4])
edges.append([1, 2, 3])
edges.append([1, 3, 2])
edges.append([1, 4, 2])
edges.append([3, 2, 5])
edges.append([3, 1, 1])
edges.append([4, 3, -3])
print(bellmanFord(edges,5,0))


# Floyd Marshall (O(V^3))
# https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab_channel=WilliamFiset
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# Dijkstra and Bellman Ford algorithms finds min distance from a source to all other nodes
# Floyd Warshall algorithm finds min distance between all pairs of nodes 


def floydMarshall(graph):
    n = len(graph)
    dist = [[float('inf') for j in range(n)] for i in range(n)]
    print(dist)

    for i in graph:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

graph = {}
for i in range(4):
    graph[i] = {}

graph[0][1] = 5
graph[1][2] = 3
graph[2][3] = 1
graph[0][3] = 10
print(floydMarshall(graph))