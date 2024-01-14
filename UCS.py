# Uniform Cost Search
path = []
parent = {}
frontier = []
visited = []
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A',1),('G1',9), ('D',4)],
    'C': [('A',4),('E',6)],
    'D': [('B',4),('G2',1)],
    'E': [('C',6),('G3',4)],
    'G1': [('B',9)],
    'G2': [('D',1)],
    'G3': [('E',4)]
}
frontier.append(('A',0,None))
while(True):
    frontier.sort(key = lambda x: x[1])
    current_node,current_cost,current_parent = frontier.pop(0)
    visited.append(current_node)
    parent[current_node] = current_parent
    if(current_node.startswith('G')):
        break
    for child, child_cost in graph[current_node]:
        if child not in visited:
            frontier.append((child,child_cost,current_node))
goal = visited[len(visited)-1]
path = [goal]
cost = 0
while(goal != 'A'):
    l = graph[goal]
    for x in l:
        if x[0] == parent[goal]:
            cost += x[1]
    goal = parent[goal]
    path.append(goal)
path.reverse()
print(path)
print(cost)
