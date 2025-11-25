def dijkstra_shortest_path(graph, start_node, end_node):
    infinity = float('inf') 
    distances = {node: infinity for node in graph}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph}
    unvisited_nodes = list(graph.keys())
    while unvisited_nodes:
        current_node = None
        min_distance = infinity

        for node in unvisited_nodes:
            if distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        if min_distance == infinity:
            break
            
        unvisited_nodes.remove(current_node)
        
        if current_node in graph:
            for neighbor, weight in graph[current_node].items():
                new_distance = distances[current_node] + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

    path = []
    if distances[end_node] != infinity:
        current = end_node
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        
        path.reverse()
        return "->".join(path)
    else:
        return None


def solve_dijkstra_problem(input_string):
    parts = input_string.split('/')
    if len(parts) != 2:
        print("Error: Invalid input format. Expected 'edges/queries'.")
        return

    edges_str, queries_str = parts
    graph = {}
    nodes = set()
    edges = edges_str.split(',')
    
    for edge in edges:
        edge = edge.strip()
        if not edge:
            continue
            
        u, weight_str, v = edge.split()
        weight = int(weight_str)
        nodes.add(u)
        nodes.add(v)
        
        if u not in graph:
            graph[u] = {}
        
        graph[u][v] = weight
        
    for node in nodes:
        if node not in graph:
            graph[node] = {}
            
    queries = queries_str.split(',')
    for query in queries:
        query = query.strip()
        if not query:
            continue

        start, end = query.split()
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
            
        result_path = dijkstra_shortest_path(graph, start, end)
        
        if result_path:
            print(f"{start} to {end} : {result_path}")
        else:
            print(f"Not have path : {start} to {end}")


input = input('Enter : ')
solve_dijkstra_problem(input)