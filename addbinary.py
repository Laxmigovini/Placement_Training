a = "1010"
b = "1011"
res = []
carry = 0
i = len(a) - 1
j = len(b) - 1
while i>=0 or j>=0 or carry:
    digita = int(a[i]) if i>=0 else 0
    digitb = int(b[j]) if j>=0 else 0
    total = digita + digitb + carry
    res.append(str(total%2))
    carry = total // 2
    i-=1
    j-=1
print("".join(reversed(res)))
