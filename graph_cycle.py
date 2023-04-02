from collections import deque

# use bfs
def undirected_cycle(adj):
    visited = [-1 for i in range(len(adj))]
    q = deque()
    q.append(0)
    while (len(q)):
        visited[q[0]]= 1
        for i in adj[q[0]]:
            if visited[i] == 0:
                return True
            if visited[i] == -1:
                q.append(i)
                visited[i] = 0
        q.popleft()
    return False


def explore(i,visited,adj):
    visited[i] = 0
    for j in adj[i]:
        if visited[j] == 0:
            return True
        if visited[j] == -1 and explore(j,visited,adj):
            return True
    visited[i] = 1
    return False

def directed_cycle(adj):
    visited = [-1 for i in range(len(adj))]
    for i in range(len(adj)):
        if visited[i] == -1:
            if explore(i,visited,adj):
                return True
    return False

a = [[1],[2],[3],[0]]
print(directed_cycle(a))


