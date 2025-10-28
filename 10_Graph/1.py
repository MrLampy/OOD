def create_directed_graph_and_get_adjacency_matrix(input_string):
    pairs = input_string.split(',')
    nodes = set()
    edges = []
    
    for pair in pairs:
        pair = pair.strip()
        if not pair:
            continue
        source, target = pair.split()
        nodes.add(source)
        nodes.add(target)
        edges.append((source, target))
   
    sorted_nodes = sorted(list(nodes))
    num_nodes = len(sorted_nodes)
    node_to_index = {node: i for i, node in enumerate(sorted_nodes)}
    
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    for source, target in edges:
        if source in node_to_index and target in node_to_index:
            source_index = node_to_index[source]
            target_index = node_to_index[target]
            adjacency_matrix[source_index][target_index] = 1

    header = "    " + "".join([f"{node:3}" for node in sorted_nodes])
    print("\n" + header)
    
    for i in range(num_nodes):
        node = sorted_nodes[i]
        row_data = adjacency_matrix[i]
        row_str = ", ".join([str(val) for val in row_data])
        print(f"{node} : {row_str}")

user_input = input('Enter : ')
create_directed_graph_and_get_adjacency_matrix(user_input)