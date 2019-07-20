import tkinter as tk

def show_entry_fields():
    name=e1.get()
    number=e2.get()
    email=e3.get()
    address=e4.get()
    gender=e5.get()
    
    
    new=str(name+":"+number+":"+email+":"+address+":"+gender+";\n")
    print(new)
    file1 = open("MyFile1.txt","a")  
    file1.write(new)
    file1.close()

master = tk.Tk()
master.configure(background='#4CBB17')
master.geometry("+500+500")
tk.Label(master, 
         text="Name",bg="White",padx=30).grid(row=0,column=1)
tk.Label(master, 
         text="Number",bg="White",padx=30).grid(row=1,column=1)
tk.Label(master, 
         text="Email",bg="White",padx=30).grid(row=2,column=1)
tk.Label(master, 
         text="Address",bg="White",padx=30).grid(row=3,column=1)
tk.Label(master, 
         text="Gender",bg="White",padx=30).grid(row=4,column=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)

e1.grid(row=0, column=3,pady=5)
e2.grid(row=1, column=3,pady=5)
e3.grid(row=2, column=3,pady=5)
e4.grid(row=3, column=3,pady=5)
e5.grid(row=4, column=3,pady=5)



tk.Button(master, 
          text='Quit', 
          command=master.quit,bg="black",fg="white").grid(row=6, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=4,padx=4)
tk.Button(master, 
          text='Submit', command=show_entry_fields).grid(row=6, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4,padx=4)

tk.mainloop()
