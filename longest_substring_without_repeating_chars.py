s="abcabcabbf"
i = 0
n = len(s)
char_set = set()
max_len = 0
for j in range(n):
    while s[j] in char_set:
        char_set.remove(s[i])
        i+=1
    char_set.add(s[j])
    max_len=max(max_len,j-i+1)
print(max_len)
