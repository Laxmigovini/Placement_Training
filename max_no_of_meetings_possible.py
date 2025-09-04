start = [0,3,8,1,5,7,9]
end = [5,6,10,2,6,9,11]
meetings = [(start[i],end[i]) for i in range(len(start))]
meetings.sort(key = lambda x: x[1])
selected = []
count = 0
last_ele = -1
for s,e in meetings:
    if s >= last_ele + 1:
        selected.append((s,e))
        last_ele = e
        count+=1
print(count)