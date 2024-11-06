import tkinter as tk
import random as r

root=tk.Tk()
root.geometry('1000x700+500+50')

def Info():
    print(en1.get())
frame1=tk.Frame(root,background='red')
frame1.pack(expand=True)


label = tk.Label(frame1, text="Xin chào!", font=("Arial", 16,'bold'), fg="blue", bg="yellow")
label.pack()

en1=tk.Entry(frame1, font=("Arial", 16,'bold'))
en1.pack()

but1=tk.Button(frame1,text='Press me',font=("Arial", 16,'bold'),command=Info)
but1.pack()

root.mainloop()