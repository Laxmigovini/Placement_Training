from tkinter import * 
root=Tk() 
root.geometry("500x500") 
root.title("Arithmetic Operations") 
 
lb0=Label(text="Arithmetic Operations",fg="red",font=("Times New Roman",18)) 
lb0.place(x=180,y=20) 
 
fno = IntVar() 
sno = IntVar() 
 
lb1=Label(text="Enter 1st Number:",font=("Times New Roman",14)) 
lb1.place(x=60,y=60) 
el0=Entry(textvariable=fno) 
el0.place(x=210,y=65) 
 
lb2=Label(text="Enter 2nd Number:",font=("Times New Roman",14)) 
lb2.place(x=60,y=95) 
el1=Entry(textvariable=sno) 
el1.place(x=210,y=95) 
 
lb3=Label(root) 
lb3.place(x=100,y=250) 
 
def add(): 
    a = fno.get()+sno.get() 
    lb3.config(font=("Times New Roman",18),text="Addition of Two number is=:"+str(a)) 
 
def sub(): 
    a = fno.get()-sno.get() 
    lb3.config(font=("Times New Roman",18),text="Subtraction of Two number is=:"+str(a)) 
 
def mul(): 
    a = fno.get()*sno.get() 
    lb3.config(font=("Times New Roman",18),text="Multiplication of Two number is=:"+str(a)) 
b=Button(font=("Times New Roman",14),text="Add", command=add)
b.place(x=150,y=170)
b0=Button(font=("Times New Roman",14),text=("Sub"), command=sub)
b0.place(x=210,y=170)
b1=Button(font=("Times New Roman",14),text=("Mul"), command=mul)
b1.place(x=270,y=170)
root.mainloop()
