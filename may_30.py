from collections import defaultdict
#printing paths using depth first search
def print_all_paths(d,u,v,path = []):
    path.append(u)
    if u == v:
        print(path)
    for i in d[u]: #here i = 2,7,8 values of 5
        if i not in path:
            print_all_paths(d,i,v,path)
    path.pop()
    return
def count_all_paths(d,u,v,path = [],c=0):
    path.append(u)
    if u == v:
        c=c+1
    for i in d[u]: #here i = 2,7,8 values of 5
        if i not in path:
            c=count_all_paths(d,i,v,path,c)
    path.pop()
    return c
def count_all_paths(d,u,v,path = set(),c=0):
    path.add(u)
    if u == v:
        c=c+1
    for i in d[u]: #here i = 2,7,8 values of 5
        if i not in path:
            c=count_all_paths(d,i,v,path,c)
    path.remove(u)
    return c
def len_all_paths(d,u,v,path = [],c=0):
    path.append(u)
    if u == v:
        print(path,c+1)
    for i in d[u]: #here i = 2,7,8 values of 5
        if i not in path:
            c=c+1
            len_all_paths(d,i,v,path)
            c=c-1
    path.pop()
    return
def check_all_paths(d,u,v,path = []):
    path.append(u)
    if u == v:
        return True
    for i in d[u]: #here i = 2,7,8 values of 5
        if i not in path:
            if check_all_paths(d,i,v,path):
                return True
    path.pop()
    return False
def BFS(d,u,v=[],path = []):
    path=[u]
    while path:
        curr=path.pop(0)
        print(curr)
        if curr not in v:
            v.append(curr)
        for i in d[curr]:
            if i not in v and i not in path:
                v.append(i)
                path.append(i)
def BFS(d,u,v,path = []):
    v1 ={5}
    path=[u]
    while path:
        curr=path.pop(0)
        if curr == v:
            return True
        for i in d[curr]:
            if i not in v1 and i not in path:
                v1.add(i)
                path.append(i)
    return False
        
graphs = [(5,2),(5,7),(5,8),(2,8),(2,7),(8,7),(8,3),(2,3)]
d = defaultdict(list)
for i,j in graphs:
    d[i].append(j)
    d[j].append(i)            
#print_all_paths(d,5,3)
#print(count_all_paths(d,5,3))
#print(count_all_paths(d,5,3))
#len_all_paths(d,5,3)
#print(check_all_paths(d,5,3))
#BFS(d,5)
print(BFS(d,5,3))
'''
d = {}
for i,j in graphs:
    if i not in d:
        d[i] = [j]
    else:
        d[i].append(j)
    if j not in d:
        d[j] = [i]
    else:
        d[j].append(i)
print(d)
'''    
