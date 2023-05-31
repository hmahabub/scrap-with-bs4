from tkinter import *

master = Tk()

mycanvas = Canvas(master)
mycanvas.pack()
for a2 in range(25):
	for a in range(5):
		for b in range(1,30):
			for b2 in range(1,30):
				x0 =((a*10)+b)+10
				y0 =(a2*10)+b2
				x1 = ((a*10)+b)+20
				y1 = ((a2*10)+b2)+10
				mycanvas.create_rectangle(x0,y0,x1,y1,fill="orange",outline="orange")

mainloop()