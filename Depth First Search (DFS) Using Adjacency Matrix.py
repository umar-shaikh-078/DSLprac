vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = []

for i in range(vertices):
    row = [0] * vertices
    graph.append(row)

print("Enter edges (u v):")

for i in range(edges):
    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[v][u] = 1

print("\nAdjacency Matrix:")

for row in graph:
    print(row)

visited = [False] * vertices

def DFS(vertex):
    visited[vertex] = True
    print(vertex, end=" ")

    for neighbour in range(vertices):
        if graph[vertex][neighbour] == 1 and not visited[neighbour]:
            DFS(neighbour)

start = int(input("\nEnter starting vertex: "))

print("DFS Traversal:")
DFS(start)

print()