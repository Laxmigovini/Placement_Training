f=open("sample.txt","x")
f.write("welcome to sr university")
f.close()
f=open("sample.txt","r")
nl=0
nw=0
nc=0
for line in f:
    line=line.strip("\n")
    words=line.split()
    nl=nl+1
    nw=nw+len(words)
    nc=nc+len(line)
f.close()
print("lines:",nl,"words:",nw,"characters:",nc)
