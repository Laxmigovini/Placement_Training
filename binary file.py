f=open("binary1.bin",'wb')
l=[9,10,4,7]
b=bytearray(l)
f.write(b)
f.close()
f=open("binary1.bin",'rb')
print(f.read())
f.close()
