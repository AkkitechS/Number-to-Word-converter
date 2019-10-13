from tkinter import *
import finalmodule as fn
import subprocess

def convert():
    val = value.get()
    print(convalue.set(fn.final(val)))

def fileOpening():
	try:
		subprocess.call(['notepad.exe', 'About.txt'])

	except:
		print("Notepad not found")

root = Tk()
root.geometry("350x100")
root.title("Number to word converter")
mymenu = Menu(root)
mymenu.add_command(label = "About", command = fileOpening)
root.config(menu = mymenu)
Label(root, text = 'Enter number(upto 9 digits)').grid(row = 0, column = 0)
Label(root, text = "converted number").grid(row = 1, column = 0)
value = StringVar()
convalue = StringVar()
Entry(root, textvariable = value).grid(row = 0, column = 1)
Entry(root, textvariable = convalue).grid(row = 1, column = 1)
Button(root, text = "Convert", command = convert).grid(row = 2, column = 2)

root.mainloop()
