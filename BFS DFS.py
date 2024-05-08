from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end='')
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)

def bfs(graph,start):
    visited= set()
    queue= deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end='')
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                
def main():
    graph={}
    n= int(input("Enter number of nodes: "))
    
    for i in range(n):
        node = input(f"Enter node {i+1}: ")
        neighbours = input(f"Enter nrighbours of {node} seperated by space: ").split()
        graph[node] = neighbours
    
    start_node = input("Enter start node: ")
    
    print('DFS = ', end='')
    dfs(graph, start_node)
    
    print("\nBFS= ", end='')
    bfs(graph, start_node)
    
main()