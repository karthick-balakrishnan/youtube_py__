import tkinter as tk

surface=tk.Tk()

#5types of button style


button_1=tk.Button(master=surface,text="FLAT",relief=tk.FLAT,width=10)
button_1.place(x=60,y=10)

button_2=tk.Button(master=surface,text="RAISED",relief=tk.RAISED,width=10)
button_2.place(x=60,y=40)

button_3=tk.Button(master=surface,text="SUNKEN",relief=tk.SUNKEN,width=10)
button_3.place(x=60,y=70)

button_4=tk.Button(master=surface,text="GROOVE",relief=tk.GROOVE,width=10)
button_4.place(x=60,y=100)

button_5=tk.Button(master=surface,text="RIDGE",relief=tk.RIDGE,width=10)
button_5.place(x=60,y=130)

surface.mainloop()
