from collections import deque

# ===== ЗАДАЧА 1: создаём граф =====
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}

# ===== ЗАДАЧА 2: добавляем вершину =====
graph['F'] = ['A', 'C']
graph['A'].append('F')

# ===== ЗАДАЧА 3: соседи вершины =====
def get_neighbors(graph, node):
    return graph.get(node, [])

# ===== ЗАДАЧА 4: DFS (рекурсивно) =====
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

    return visited

# ===== ЗАДАЧА 5: DFS (через стек) =====
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            stack.extend(graph[node])

    return visited

# ===== ЗАДАЧА 6: BFS (через очередь) =====
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            queue.extend(graph[node])

    return visited

# ===== ЗАДАЧА 8: проверка пути =====
def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path(graph, neighbor, end, visited):
                return True

    return False

# ===== ЗАДАЧА 9: количество достижимых =====
def count_reachable(graph, start):
    visited = bfs(graph, start)
    return len(visited)

# ===== ЗАДАЧА 10: кратчайший путь =====
def shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


# ===== ЗАДАЧА 7: запуск программы =====
start = input("Введите стартовую вершину: ")
end = input("Введите конечную вершину: ")

print("\nСоседи вершины:", get_neighbors(graph, start))

print("\nDFS (рекурсивно):")
dfs_recursive(graph, start)

print("\n\nDFS (стек):")
dfs_stack(graph, start)

print("\n\nBFS:")
bfs(graph, start)

print("\n\nПуть существует:", has_path(graph, start, end))

print("\nКоличество достижимых вершин:", count_reachable(graph, start))

print("\nКратчайший путь:", shortest_path(graph, start, end))