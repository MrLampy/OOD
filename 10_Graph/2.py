def create_undirected_graph_and_traverse(input_string):
    pairs = input_string.split(',')
    adj_list = {}
    nodes = set()
    
    for pair in pairs:
        pair = pair.strip()
        if not pair:
            continue
        u, v = pair.split()
        nodes.add(u)
        nodes.add(v)
        
        if u not in adj_list: adj_list[u] = []
        if v not in adj_list: adj_list[v] = []
        if v not in adj_list[u]: adj_list[u].append(v)
        if u not in adj_list[v]: adj_list[v].append(u)
        
    if not nodes:
        print("Depth First Traversals :")
        print("Bredth First Traversals :")
        return
        
    start_node = sorted(list(nodes))[0] 
    
    for node in adj_list:
        adj_list[node].sort() 

    all_visited = set()
    dft_result = []

    for component_start_node in sorted(list(nodes)):
        if component_start_node not in all_visited:
            stack = [component_start_node]
            
            while stack:
                u = stack.pop()
                
                if u not in all_visited:
                    all_visited.add(u)
                    dft_result.append(u)
                    
                    neighbors = adj_list.get(u, [])
                    for v in reversed(neighbors):
                        if v not in all_visited:
                            stack.append(v)
                            
    all_visited_bft = set()
    bft_result = []

    for component_start_node in sorted(list(nodes)):
        if component_start_node not in all_visited_bft:
            queue = [component_start_node]
            all_visited_bft.add(component_start_node)
            bft_result.append(component_start_node)
            
            while queue:
                u = queue.pop(0)
                
                for v in adj_list.get(u, []):
                    if v not in all_visited_bft:
                        all_visited_bft.add(v)
                        bft_result.append(v)
                        queue.append(v)

    print(f"Depth First Traversals : {' '.join(dft_result)}")
    print(f"Bredth First Traversals : {' '.join(bft_result)}")

if  __name__ == '__main__':
    input = input('Enter : ')
    create_undirected_graph_and_traverse(input)