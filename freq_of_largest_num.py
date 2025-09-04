a=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i] = 1
max_value = 0
value = 0
for key in freq:
    if max_value<freq[key]:
        max_value=freq[key]
        value = key
print(value)