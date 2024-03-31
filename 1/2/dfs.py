from collections import defaultdict
adj=defaultdict(list)
def add_edge(u,v):
    adj[u].append(v)
def dfs(root,visited):
    print(root,end=" ")
    for node in adj[root]:
        if node not in visited:
            dfs(node,visited)
            visited.add(node)
            
add_edge(5,3)
add_edge(5,7)
add_edge(3,2)
add_edge(3,4)
add_edge(4,8)
add_edge(7,8)

visited=set()
dfs(5,visited)
print()
    
