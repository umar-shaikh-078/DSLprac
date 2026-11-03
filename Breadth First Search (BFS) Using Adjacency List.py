from collections import deque

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = {}

for i in range(vertices):
    graph[i] = []

print("Enter edges (u v):")

for i in range(edges):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = set()
queue = deque()

queue.append(start)
visited.add(start)

print("BFS Traversal:")

while queue:
    vertex = queue.popleft()
    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)

print()