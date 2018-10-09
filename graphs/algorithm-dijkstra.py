# Dijkstra's algorithm for search short path in graph
# Asymptotic complexity (O) = V * V + E = V**2, where V - count vertex, E - count edges


def algorithm_dijkstra():
    """
    :rtype None
    """
    node = find_lowest_cost_node()

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node()


def find_lowest_cost_node():
    """
    :rtype dict
    """
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def print_short_path():
    if costs['fin'] == float('inf') or parents['fin'] is None:
        print('Short path from Start to Fin not exist.')
    path = ['fin']
    value = parents['fin']
    path = [value] + path
    path = [parents[value]] + path
    path = [parents[parents[value]]] + path
    print('Path from Start to Fin: {}; short cost {}.'.format('->'.join(path), costs['fin']))


graph = {
    'start': {'a': 6, 'b': 2},
    'a': {'fin': 1},
    'b': {'a': 3, 'fin': 5},
    'fin': {}
}

costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

processed = []

algorithm_dijkstra()
print_short_path()
