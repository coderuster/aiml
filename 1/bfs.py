from collections import defaultdict,deque
adj=defaultdict(list)
def add_edge(u,v):
    adj[u].append(v)

def bfs(root):
    q=deque([])
    q.append(root)
    visited=set()
    visited.add(root)
    while q:
        top=q.popleft()
        print(top,end=" ")
        for child in adj[top]:
            if(child not in visited):
                q.append(child)
                visited.add(child)
    print()

add_edge(5,3)
add_edge(5,7)
add_edge(3,2)
add_edge(3,4)
add_edge(4,8)
add_edge(7,8)

bfs(5)
    
