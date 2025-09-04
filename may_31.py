from collections import defaultdict
def Dijkstra_sssp(u):
    dis = defaultdict(lambda : float('inf'))
    dis[u] = 0
    q=[u]
    vi =set()
    while q:
        n=q.pop(0)
        vi.add(n)
        for i,w in d[n]:
            if dis[n]+w < dis[i]:
                dis[i] = dis[n]+w
            if i not in q and i not in vi:
                q.append(i)
    return dis
def Dijkstra_sp(u,v):
    dis = defaultdict(lambda : float('inf'))
    sp = defaultdict(int)
    sp[u]=u
    dis[u] = 0
    q=[u]
    vi =set()
    while q:
        n=q.pop(0)
        vi.add(n)
        for i,w in d[n]:
            if dis[n]+w < dis[i]:
                dis[i] = dis[n]+w
            if i not in q and i not in vi:
                q.append(i)
    l = [v]
    while(sp[v]!=v):
        l.append(sp[v])
        v=sp[v]
    return (l[::-1])

from collections import defaultdict
import heapq
def mst_prims(u):
    heap = [(0,u)]
    mincost = 0
    visited = set()
    while heap:
        w,curr = heapq.heappop(heap)
        if curr in visited:
            continue
        visited.add(curr)
        mincost += w
        for i,w in d[curr]:
            if i not in visited:
                heapq.heappush(heap,(w,i))
def sp_prims(u):
    heap = [(0,u)]
    mincost = 0
    visited = set()
    l=[]
    while heap:
        w,curr = heapq.heappop(heap)
        if curr in visited:
            continue
        l.append(curr)
        visited.add(curr)
        mincost += w
        for i,w in d[curr]:
            if i not in visited:
                heapq.heappush(heap,(w,i))
    print(l)
    print(mincost)
    
edges = [(10,5,2),(10,7,4),(5,7,1),(7,8,1),(5,8,3),(5,3,2),(8,3,1)]
d = defaultdict(list)
for i,j,w in edges:
    d[i].append([j,w])
    d[j].append([i,w])
#xprint(Dijkstra_sssp(10))
#print(Dijkstra_sp(10,3))
#print(mst_prims(10))
sp_prims(10)
