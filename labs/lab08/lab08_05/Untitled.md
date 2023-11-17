---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python

```

```python
# Обход (поиск) в глубину
def dfs_depth(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)
        for next in graph[start]:
            dfs_depth(graph,next,visited)
    return visited


graph = {
    'A':['B','S'],
    'B':['A'],
    'C':['D','E','F','S'],
    'D':['C'],
    'E':['C','H'],
    'F':['C','G'],
    'G':['F','S'],
    'H':['E','G'],
    'S':['A','C','G']
}
print("~~~~test_depth~~~~")
print(dfs_depth(graph, 'A'))
```

```python
# Обход (поиск) в ширину
from collections import deque
def bfs_breadth(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


print("~~~~test_breadth~~~~")
print(bfs_breadth(graph, 'A'))
```

```python
# Нахождение эйлерова цикла
def find_eulerian_cycle(graph):
    stack = []
    cycle=[]
    start_vertex = list(graph.keys())[0]
    while True:
        if len(graph[start_vertex])==0:
            cycle.append(start_vertex)
            if len(stack)==0:
                break
            start_vertex=stack.pop()
        else:
            stack.append(start_vertex)
            neighbor=graph[start_vertex][0]
            graph[start_vertex].remove(neighbor)
            graph[neighbor].remove(start_vertex)
            start_vertex=neighbor
    return cycle[::-1]

print("~~~~test_find_eulerian_cycle~~~~")
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(find_eulerian_cycle(graph))
```

```python
# Нахождение гамильтонова цикла
def is_valid(v, pos, path, graph):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos+1) == True:
                return True
            path[pos] = -1
    return False

def hamiltonian_cycle(graph):
    n = len(graph)
    path = [-1] * n
    path[0] = 0
    if hamiltonian_cycle_util(graph, path, 1) == False:
        print("Гамильтонов цикл не существует")
        return False
    print("Гамильтонов цикл существует:")
    for vertex in path:
        print(vertex, end=" ")
    print(path[0])
    return True

print("~~~~test_hamiltonian_cycle~~~~")
# Матрица смежности графа
graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 0]]

hamiltonian_cycle(graph)
```

```python
# Алгоритм Дейкстры
import heapq
def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

print("~~~~test_dijkstra~~~~")
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))
```

```python
# Задание
import heapq
def dijkstra_two(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances[end]

print("~~~~test_dijkstra_two~~~~")
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

print("Кротчайший путь =", dijkstra_two(graph, 'A', 'D'))
```

```python
# Задание 1
graph1={
    '1': {'2': 10, '3': 12},
    '2': {'3': 1, '4': 11, '5': 3},
    '3': {'6': 8, '7': 10},
    '4': {'6': 1},
    '5': {'7': 9},
    '6': {'7': 2},
    '7': {}
}

print("Кротчайший путь =", dijkstra_two(graph1, '2', '6'))
print("\n")

# Задание 2
graph2={
    '1': {'2': 14, '6': 8},
    '2': {'1': 14, '3': 5, '4': 10, '5': 2, '6': 2, '8': 9},
    '3': {'2': 5, '8': 11},
    '4': {'2': 10, '5': 3, '6': 6, '7': 5},
    '5': {'2': 2, '4': 3, '7': 8, '8': 1},
    '6': {'1': 8, '2': 2, '4': 6, '7': 5},
    '7': {'4': 5, '5': 8, '6': 5, '8': 7},
    '8': {'2': 9, '3': 11, '5': 1, '7': 7}
}

print("Кротчайший путь =", dijkstra_two(graph2, '3', '8'))
```

```python

```

```python

```

```python

```

```python

```
