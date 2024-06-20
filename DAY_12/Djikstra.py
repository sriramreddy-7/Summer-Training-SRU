def dijkstras(g, x):
    d = {node: x for node in g}
    d[x] = 0
    q = [x]
    v = set()

    while q:
        current_distance = x
        current_index = 0
        for i in range(len(q)):
            if d[q[i]] < current_distance:
                current_distance = d[q[i]]
                current_index = i

        x = q.pop(current_index)

        if x in v:
            continue

        v.add(x)

        for neighbor, weight in g[x]:
            distance = current_distance + weight
            if distance < d[neighbor]:
                d[neighbor] = distance
                if neighbor not in v:
                    q.append(neighbor)

    return v, d


g = {
    5: [(3, 1), (1, 2), (6, 3)],
    1: [(5, 2), (2, 1)],
    3: [(5, 1), (6, 3)],
    6: [(3, 3)],
    2: [(1, 1)]
}
visited_nodes, distances = dijkstras(g, 1)
print("Visited Nodes:", visited_nodes)
print("Distances:", distances)
