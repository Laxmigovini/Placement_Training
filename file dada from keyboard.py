'''press 1.create a file
press 2.write content to file
press 3.add content to the file
press 4.display the content of te file
press 5.delete a file'''
print("press1.create a file")
print("press2.write content to the file")
print("press3.add content to file")
print("press4.display the content of the file")
print("press5.delete a file")
while(input("do you want to continue[y/n]:")=='y'):
    choice=int(input("enter your choice:"))
    if choice==1:
        f=open("example.txt",'x')
        print("file created sucessfully")
    elif choice==2:
        f=open("example.txt",'w')
        data=input("enter data:")
        f.write(data)
        f.close()
        print("content written sucessfully")
    elif choice==3:
        f=open("example.txt",'a')
        data=input("enter data to be added:")
        f.write(data)
        f.close()
        print("content added sucessfully")
    elif choice==4:
        f=open("example.txt",'r')
        print(f.read())
        f.close()
    elif choice==5:
        import os
        if os.path.exists("example.txt"):
            os.remove("example.txt")
            print("file removed sucessfully")
        else:
            print("file not found")
    else:
        print("enter correct choice")
