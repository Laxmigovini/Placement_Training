a = "abcdefbgh"
i = 0
n = len(a)
char_set = set()
max_len=0
for j in range(n):
    while a[j] in char_set:
        char_set.remove(a[i])
        i+=1
    char_set.add(a[j])
    max_len=max(max_len,j-i+1)
print(max_len)
