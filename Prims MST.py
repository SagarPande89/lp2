from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        visited = set()
        min_span_tree = []

        # Start Prim's algorithm from the first vertex
        start_vertex = next(iter(self.graph.keys()))
        visited.add(start_vertex)

        while len(visited) < len(self.graph):
            min_weight = float('inf')
            min_edge = None

            # Find the minimum edge connecting visited and unvisited vertices
            for u in visited:
                for v, weight in self.graph[u].items():
                    if v not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (u, v)

            # Add the minimum edge to the minimum spanning tree
            min_span_tree.append((min_edge, min_weight))
            visited.add(min_edge[1])

        return min_span_tree

def main():
    graph = Graph()

    # User input for number of nodes
    num_nodes = int(input("Enter the number of nodes: "))

    # User input for edges
    for _ in range(num_nodes):
        node = input(f"Enter node and its connections (format: node connected_node1 weight1 connected_node2 weight2 ...): ")
        node_data = node.split()
        u = node_data[0]
        for i in range(1, len(node_data), 2):
            v = node_data[i]
            weight = int(node_data[i + 1])
            graph.add_edge(u, v, weight)

    min_span_tree = graph.prim_mst()

    print("Minimum Spanning Tree:")
    total_weight = 0
    for edge, weight in min_span_tree:
        u, v = edge
        print(f"Edge: {u} -- {v}, Weight: {weight}")
        total_weight += weight
    print(f"Total weight of Minimum Spanning Tree: {total_weight}")

if __name__ == "__main__":
    main()