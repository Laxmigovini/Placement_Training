from collections import defaultdict
def print_all_paths(d,u,v,path = []):
    path.append(u)
    if u == v:
        print(path)
    for i,w in d[u]:
        if i not in path:
            print_all_paths(d,i,v,path)
    path.pop()
    return
def print_weights(d,u,v,path = [],cost = 0):
    path.append(u)
    if u == v:
        print(path,cost)
    for i,w in d[u]:
        if i not in path:
            cost = cost+w
            print_weights(d,i,v,path,cost)
            cost = cost - w
    path.pop()
    return
edges = [(5,2,3),(5,7,2),(5,8,1),(2,7,2),(2,8,4),(7,8,1),(2,3,2),(8,3,3)]
d = defaultdict(list)
for i,j,w in edges:
    d[i].append([j,w])
    d[j].append([i,w])
#print_all_paths(d,5,3)
print_weights(d,5,3)
