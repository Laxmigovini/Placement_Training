ip = "hippopotamus"
i = 0
j = len(ip) -1
ip = list(ip)
vowels = "aeiou"
while i < j:
    if ip[i] in vowels:
        i+=1
    if ip[j] in vowels:
        j-=1
    if ip[i] or ip[j] not in vowels:
        ip[i],ip[j] = ip[j],ip[i]
        i+=1
        j-=1
print("".join(ip))