# A * Search
path = []
parent = {}
frontier = []
visited = []
graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2), ('E', 4), ('A',3)],
    'C': [('F', 6), ('A',5)],
    'D': [('G', 4), ('B',2)],
    'E': [('H', 5), ('B',4)],
    'F': [('I', 3), ('C',6)],
    'G': [('D',4)],
    'H': [('E',5)],
    'I': [('F',3)]
}

heuristic_values = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 4,
    'E': 6,
    'F': 4,
    'G': 0,  
    'H': 0,
    'I': 0
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
            cost = 0
            c_node = current_node
            ch_node = child
            while(ch_node != 'A'):
                l = graph[c_node]
                for x in l:
                    if(x[0] == ch_node):
                        cost += x[1]
                        break
                ch_node = c_node
                c_node = parent[c_node]
            frontier.append((child,cost+heuristic_values[child],current_node))
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
