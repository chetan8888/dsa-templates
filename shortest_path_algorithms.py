from queue import PriorityQueue
import math

# For DAG use simple BFS to find shortest distance (O(V+E))

# Ddstikstra Algorithm (O((V+E)logV)).
# finds shortest path from source to all other nodes
# Practical Uses: Network Routing Protocols, Biology (spread of viruses among humans)

# GREEDY
# graph => 1:[[0,2],[3,4]]   1 has 2 neighbors 0 and 3 at distances 2 and 4
# Djikstra works only for positive edges. For negative edges use Bellman Ford
# O((V+E)logV)

# Leetcode Questions: https://leetcode.com/list/53js48ke/

def djikstra(graph,source,target,n):
    dist = [9999999 for i in range(n)]
    pq = PriorityQueue()
    dist[source] = 0
    pq.put((0,source))

    while not pq.empty():
        currDist, currNode = pq.get()
        if dist[currNode] >= currDist:
            for neighbor in graph[currNode]:
                if dist[neighbor[0]] > dist[currNode] + neighbor[1]:
                    dist[neighbor[0]] = dist[currNode] + neighbor[1]
                    pq.put((dist[neighbor[0]],neighbor[0]))
    return dist[target]

graph = {}
graph[0] = [[1,1],[3,10]]
graph[1] = [[2,2]]
graph[2] = [[3,4]]
graph[3] = []
print(djikstra(graph,0,3,4))


# Bellman Ford (O(V*E))
# Dynamic Programming
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
# Be careful of negative cycles

# The idea is, assuming that there is no negative weight cycle if we have calculated shortest paths with at most i edges, then an iteration over all edges guarantees to give the shortest path with at-most (i+1) edges. Dynamic Programming Optimum Substructure property.

# Leetcode Questions: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

def bellmanFord(edges, n, source):
    dist = [math.inf for i in range(n)]
    dist[source] = 0

    # There can be maximum |V| – 1 edges in any simple path, that is why the outer loop runs |V| – 1 times. 
    for i in range(n-1):
        update = False
        for u,v,w in edges:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                update = True
        if not update:
            break
    
    # To detect a negative cycle, simply check if an additional iteration of outer loop does any update or not. If we get a shorter path, then there is a negative cycle.
    for u,v,w in edges:
        if dist[v] < dist[u]+w:
            print("Graph Contains Negative Cycle")
            return -1
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

# Dijkstra and Bellman Ford algorithms finds min distance from a source to all other nodes
# Floyd Warshall algorithm finds min distance between all pairs of nodes 

# Floyd Marshall (O(V^3))
# https://www.youtube.com/watch?v=4NQ3HnhyNfQ&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=21&ab_channel=WilliamFiset
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
# Dynamic Programming, Optimum Substructure. Taking each vertext as an intermediate vertex, we can find shortest path between any two vertices. If the optimum path between i and j contains a vertex k, then this optimum path is the combination of optimum path from i to k and optimum path from k to j.

# Leetcode Question: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

def floydMarshall(graph):
    n = len(graph)
    dist = [[float('inf') for j in range(n)] for i in range(n)]
    print(dist)

    for i in graph:
        dist[i][i] = 0
        for j in graph[i]:
            dist[i][j] = graph[i][j]

    for intermediateVertex in range(n):
        for src in range(n):
            for dst in range(n):
                dist[src][dst] = min(dist[src][dst], dist[src][intermediateVertex] + dist[intermediateVertex][dst])

    for i in range(n):
        if (dist[i][i] < 0):
            print("Graph contains negative weight cycle")
            return -1
        
    return dist

graph = {}
for i in range(4):
    graph[i] = {}

graph[0][1] = 5
graph[1][2] = 3
graph[2][3] = 1
graph[0][3] = 10
print(floydMarshall(graph))