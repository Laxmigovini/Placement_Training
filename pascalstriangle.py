def pascalstriangle(numrows):
    triangle = []
    for rowidx in range(numrows):
        row = [1]*(rowidx+1)
        for colidx in range(1,rowidx):
            row[colidx]=triangle[rowidx-1][colidx-1] + triangle[rowidx-1][colidx]
        triangle.append(row)
    return triangle
print(pascalstriangle(5))

def reverse(a):
    i = 0
    j = len(a)-1
    a=list(a)
    vowels = "aeiou"
    while i < j:
        if a[i] in vowels:
            i+=1
        if a[j] in vowels:
            j-=1
        if a[i] or a[j] not in vowels:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
    return "".join(a)
print(reverse("hippopotamus")) 

'''import math
def pascals(numrows):
    for n in range(numrows):
        row = []
        for k in range(n+1):
            value = math.comb(n,k)
            row.append(value)
    return row
print(pascals(5))'''