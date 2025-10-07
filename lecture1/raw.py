# Simple DFS implementation (with tabs and noise)

def dfs(graph, start, visited=None):

	if visited is None:

		visited = set()

	# mark visited

	visited.add(start)

	for neighbor in graph.get(start, []):

		if neighbor not in visited:

			dfs(graph, neighbor, visited)

	return visited

# sample graph

graph = {

	'A': ['B', 'C'],

	'B': ['D'],

	'C': ['E'],

	'D': [],

	'E': []

}

start = 'A'

result = dfs(graph, start)

print(sorted(result))

