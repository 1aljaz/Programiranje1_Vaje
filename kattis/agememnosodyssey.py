# https://open.kattis.com/problems/agamemnonsodyssey
from collections import defaultdict, deque

def solve():
    n, k = map(int, input().split())
    edges = []
    graph = defaultdict(list)
    
    # Read edges and build graph
    for i in range(n-1):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    # If k > 1, we can collect all resources
    if k > 1:
        return sum(c for _, _, c in edges)
    
    # For k = 1, we need to find the maximum path
    def find_longest_path(start):
        visited = set()
        max_resources = 0
        
        def dfs(node, resources):
            nonlocal max_resources
            max_resources = max(max_resources, resources)
            
            for next_node, edge_idx in graph[node]:
                if edge_idx not in visited:
                    visited.add(edge_idx)
                    dfs(next_node, resources + edges[edge_idx][2])
                    visited.remove(edge_idx)
        
        dfs(start, 0)
        return max_resources
    
    # Try all possible starting points
    return max(find_longest_path(start) for start in range(1, n+1))

print(solve())

