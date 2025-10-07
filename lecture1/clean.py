def name_dfs(name_graph, name_start, name_visited=None):
    if name_visited is None:
        name_visited = set()
    name_visited.add(name_start)
    for name_neighbor in name_graph.get(name_start, []):
        if name_neighbor not in name_visited:
            name_dfs(name_graph, name_neighbor, name_visited)
    return name_visited
name_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['E'], 'D': [], 'E': []}
name_start = 'A'
name_result = name_dfs(name_graph, name_start)
print(sorted(name_result))
