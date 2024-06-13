'''def fun(d, a, l):
    if a not in l:
        l.append(a)
        for i in d[a]:
            fun(d, i, l)
d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}
l = []
fun(d, 5, l)
print(l)'''

# possible path

''''def find_all_paths(d, start, end, path=[]):
    path = path + [start] 
    if start == end:
        return [path]
    if start not in d:
        return [] 
    paths = []  
    for node in d[start]: 
        if node not in path:  
            newpaths = find_all_paths(d, node, end, path)  
            for newpath in newpaths:
                paths.append(newpath)  
    return paths

d = {5: [7, 3], 7: [5, 4, 3], 4: [7, 8, 2], 8: [3, 4, 2], 3: [5, 7, 8], 2: [4, 8]}


all_paths = find_all_paths(d, 5, 2)
for path in all_paths:
    print(path)'''


# cost of the graph
def find_all_paths_with_costs(d, start, end, path=[], cost=0):
    path = path + [start]
    if start == end:
        return [(path, cost)]
    if start not in d:
        return []
    paths = []

    for (node, weight) in d[start]:
        if node not in path:
            newpaths = find_all_paths_with_costs(d, node, end, path, cost + weight)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


d = {
    5: [(7, 2), (3, 3)],
    7: [(5, 2), (4, 1), (3, 2)],
    4: [(7, 1), (8, 3), (2, 1)],
    8: [(3, 2), (4, 3), (2, 2)],
    3: [(5, 3), (7, 2), (8, 2)],
    2: [(4, 1), (8, 2)]
}

all_paths_with_costs = find_all_paths_with_costs(d, 5, 2)
for path, cost in all_paths_with_costs:
    print(f"Path: {path}, Cost: {cost}")

