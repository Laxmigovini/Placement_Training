from collections import defaultdict
def dfs(d,u,v,path = []):
    path.append(u)
    if u == v:
        print(path)
    for i in d[u]:
        if i not in path:
            dfs(d,i,v,path)
    path.pop()
    return
def bfs(d,u,v=[],path=[]):
    path = [u]
    while path:
        curr = path.pop()
        print(curr)
        if curr not in v:
            v .append(curr)
        for i in d[curr]:
            if i not in v and i not in path:
                v.append(i)
                path.append(i)
    
graphs = [(5,2),(5,7),(5,8),(2,8),(2,7),(8,7),(8,3),(2,3)]
d = defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)
#dfs(d,5,3)
bfs(d,5)
