from tkinter import *
ventana = Tk()
ventana.title("AUGUS IDE")
label = Label(ventana,text='hola mundo')
label.place(x= 10,y=10)
textbox = Text(ventana)
textbox.place(x=10,y=40)
textbox.insert(INSERT,"this should be red")
textbox.pack()
value = textbox.get(1.0)
textbox.tag_add("here",1.0,1.4)
textbox.tag_config("here", background="yellow", foreground="blue")
textbox.tag_config("start", background="black", foreground="green")


ventana.mainloop()



