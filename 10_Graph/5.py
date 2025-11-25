def detect_cycle_in_directed_graph(input_string):
    edges = input_string.split(',')
    adj_list = {}
    nodes = set()
    
    for edge in edges:
        edge = edge.strip()
        if not edge:
            continue
        
        try:
            u_str, v_str = edge.split()
            u, v = u_str.strip(), v_str.strip()
        except ValueError:
            print(f"Error: Invalid edge format '{edge}'. Expected 'Source Destination'.")
            return

        nodes.add(u)
        nodes.add(v)
        
        if u not in adj_list:
            adj_list[u] = []
        
        adj_list[u].append(v)
        
    for node in nodes:
        if node not in adj_list:
            adj_list[node] = []

    visited = set()
    recursion_stack = set()
    
    def dfs_check_cycle(u):
        if u in recursion_stack:
            return True
        
        if u in visited:
            return False
        
        visited.add(u)
        recursion_stack.add(u)
        
        for v in adj_list.get(u, []):
            if dfs_check_cycle(v):
                return True
        
        recursion_stack.remove(u)
        return False

    sorted_nodes = sorted(list(nodes))
    
    for node in sorted_nodes:
        if node not in visited:
            if dfs_check_cycle(node):
                print("Graph has a cycle")
                return

    print("Graph has no cycle")

input1 = input('Enter : ')
detect_cycle_in_directed_graph(input1)