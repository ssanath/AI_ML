# Depth Limited Search
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
    parent = {v:None}
    depth = {v:0}
    depth_limit = int(input("Enter the depth limit: "))
    goal = input("Enter the goal node: ")
    def recursive_dfs(v):
        visited.append(v)
        if(v == goal):
            print("Goal state reached at depth ", depth[v])
            return True
        if(depth[v] < depth_limit):
            for neighbor in graph[v]:
                if neighbor not in visited:
                    if(recursive_dfs(neighbor)):
                        return True
        return False
    def calc_depth(v):
        for neighbor in graph[v]:
            parent[neighbor] = v
            depth[neighbor] = depth[parent[neighbor]]+1
            calc_depth(neighbor)
    calc_depth(v)
    if not recursive_dfs(v):
        print("Goal state could not be reached")
dfs('A')
