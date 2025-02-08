from tkinter import *

root = Tk()
root.attributes("-fullscreen", True)
root.title("Gerenciador de Tarefas")

frame1 = Frame(root, bg="black")
frame1.place(relwidth=1, relheight=1)

def show():
	

	description=0
	status=0
	data=0

titulo = Button(frame1, text="Gerenciador de Tarefas", width=90, fg="white", bg="black", font=("Helvetica", 24), command=show)
titulo.pack(side="top")

root.mainloop()
