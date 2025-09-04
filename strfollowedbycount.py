a="aaabbaaaacccddeff"
s = ""
count = 1
n=len(a)
for i in range(0,n-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        s=s+a[i]+str(count)
        count = 1
s=s+a[i]+str(count)
print(list(s))


