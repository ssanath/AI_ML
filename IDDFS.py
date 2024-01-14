#Iterative deepening depth first search
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

def dfs(v):
    visited = []
    depth_limit = 0
    goal = input("Enter the goal state: ")
    if(goal not in graph):
        print("Goal state cannot be reached")
        return
    depth = {v:0}
    parent = {v: None}
    stack = [v]
    new_node = 'A'
    def iddfs(node):
        nonlocal new_node, depth_limit
        while(stack):
            new_node = stack.pop()
            if(new_node == goal):
                print(f"Goal state reached at depth {depth_limit}")
                return True
            for neighbor in graph[new_node]:
                if(neighbor not in stack and depth[neighbor] <= depth_limit):
                    stack.append(neighbor)
            if(stack == [] and new_node != goal):
                stack.append(v)
                depth_limit += 1
    def calc_depth(node):
        for neighbor in graph[node]:
            parent[neighbor] = node
            depth[neighbor] = depth[parent[neighbor]]+1
            calc_depth(neighbor)
    calc_depth(v)
    iddfs(v)
dfs('A')
