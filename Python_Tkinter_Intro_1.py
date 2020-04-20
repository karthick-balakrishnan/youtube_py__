import tkinter as tk

surface=tk.Tk()
surface.geometry(newGeometry="500x350+370+180")
surface.title("GUI INTERFACE")

username_label=tk.Label(master=surface,text="username",width=10,fg="black",bg="seashell3",font=("century",10))
username_label.place(x=100,y=100)

password_label=tk.Label(master=surface,text="password",width=10,fg="black",bg="seashell3",font=("century",10))
password_label.place(x=100,y=150)

username=tk.Entry(master=surface,width=20)
username.place(x=250,y=100)

password=tk.Entry(master=surface,width=20)
password.place(x=250,y=150)

ok_button=tk.Button(master=surface,text="ok",width=10,fg="black",bg="seashell3")
ok_button.place(x=200,y=250)


surface.mainloop()

