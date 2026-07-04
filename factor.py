import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
root=tkinter.Tk()
root.geometry("400x400")
root.title("factorial calculator")
inf=tkinter.LabelFrame(root,text="🧮✨✨✨🧮Factorial Calculator🧮✨✨✨🧮",font=("Arial",40,"italic","bold"),bg="#2b2b40",fg="#C3A7E7")
inf.pack(padx=10,pady=10,ipadx=350,ipady=5)
label1=tkinter.Label(inf,text="✨✨🧮Enter a Number🧮✨✨",font=("Arial",40,"italic","bold"),fg="#B03A69")
label1.pack(padx=10)
entry1=tkinter.Entry(inf,font=(40))
entry1.pack(ipadx=60,ipady=20,padx=10,pady=10)
def calculate(event=None):
    l2.config(text="RESULT")
    try:
        n=int(entry1.get())
        if n==0 or n==1:
            messagebox.showinfo("Special Result","✨✨🧮The factorial of 1 or 0 is 1🧮✨✨")
        elif n<0:
            messagebox.showwarning("warning","🚨Negative value is not allowded!🧮")
        elif n>201:
            messagebox.showwarning("Warning","🚨The number is too large!🧮")
        else:
            f=1
            for i in range(2,n+1):
                f=f*i
            l2.config(text=f"{f}")
    except ValueError:
        messagebox.showwarning("warning","🚨Enter the correct value!🧮")
b1=tkinter.Button(inf,text="🧮Calculate🧮",font=("Arial",20,"italic","bold"),command=calculate,bg="#03dac6")
b1.pack(pady=40,anchor="s") 
rl=tkinter.LabelFrame(root,text="🧮✨✨✨✨🧮Factorial is🧮✨✨✨✨🧮",font=("Arial",40,"italic","bold"),bg="#bb86fc",fg="#570CD8")
rl.pack(ipadx=350,ipady=20)
l2=tkinter.Label(rl,text="🧮✨✨🧮RESULT🧮✨✨🧮",font=("Arial",20,"italic","bold"),wraplength=1200,bg="#1E1E54",fg="#03dac6")
l2.pack()
root.configure(bg="#414163")
appic=tkinter.PhotoImage(file=r"C:\python\fa.ico")
root.iconphoto(False,appic)
root.bind('<Return>',calculate)
root.mainloop()