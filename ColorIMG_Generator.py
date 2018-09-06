# Color IMG Generator
# Released under MIT license
#
# bytebitter [at] gmail [dot] com


from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import askdirectory
import configparser
from Image_Cl import COLOR



class GUI(object):
	def __init__(self, master):
		self.ARR = []
		self.counter = 0
		self.lbox_indx = None
		self.dir_pth = "./"
		self.frame = Frame(master)
		
		self.libox = Listbox(self.frame)
		self.libox.bind("<<ListboxSelect>>", self.libox_callback)
		self.libox.grid(column = 1, row = 1, rowspan = 5, columnspan = 5, sticky="EW")
		self.en_nm = Entry(self.frame, width=10)
		self.en_nm.grid(column = 1, row = 6, columnspan = 3)
		self.btn_pl = Button(self.frame, text="+", comman=self.add_en).grid(column=4, row=6)
		self.btn_min = Button(self.frame, text="-", command=self.rem_en).grid(column=5, row=6)

		self.cl_lbl = Label(self.frame, text="Color:").grid(column=1, row=7, columnspan=3, stick=W)
		self.cl_cv = Canvas(self.frame, width=50, height=15, bg="black")
		self.cl_cv.bind("<Button-1>", self.sel_cl)
		self.cl_cv.grid(column=4, row=7, columnspan=2)

		self.var = StringVar(master)
		self.var.set("5")
		List = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
		self.bdr_lbl = Label(self.frame, text="Border:").grid(column=1, row=8, columnspan=3, stick=W)
		self.om = OptionMenu(self.frame, self.var, *List).grid(column=4, row=8, columnspan=2)

		self.divider = Canvas(self.frame, width=2, height=250, bg="grey").grid(column=6, row=1, rowspan=8)

		self.dir_lb = Label(self.frame, text="Directory:").grid(column=7, row=1, stick=W)
		self.btn_dir = Button(self.frame, text="Select", command=self.sel_dir).grid(column=8, row=1, sticky="ew")
		self.dir = Label(self.frame, text="./")
		self.dir.grid(column=7, row=2, columnspan=2)

		self.process = Button(self.frame, text="Process", command=self.proc).grid(column=7, row=4, columnspan=2, sticky="ew")


		self.frame.pack()

	def libox_callback(self, ev):
		w = ev.widget
		self.lbox_indx = int(w.curselection()[0])
		hex = self.ARR[self.lbox_indx].hex
		self.cl_cv.configure(bg=hex)

	def add_en(self):
		name = str(self.en_nm.get())
		if name != "":
			self.counter +=1
			cl_obj = COLOR(name)
			self.ARR.append(cl_obj)
			for i in range(self.libox.size()):
				self.libox.delete(0, END)
			for item in self.ARR:
				self.libox.insert(END, item.name)
			self.en_nm.delete(0, END)
			self.lbox_indx = None

	def rem_en(self):
		if self.lbox_indx != None:
			self.ARR.pop(self.lbox_indx)
			for i in range(self.libox.size()):
				self.libox.delete(0, END)
			for item in self.ARR:
				self.libox.insert(END, item.name)
			self.lbox_indx = None

	def sel_cl(self, event):
		if self.lbox_indx != None:
			rgb, hex = askcolor()
			self.cl_cv.configure(bg=hex)
			self.ARR[self.lbox_indx].set_hex(hex)

	def sel_dir(self):
		dir = askdirectory()
		self.dir.config(text=dir)
		self.dir_pth = dir


	def proc(self):
		if self.libox.size() != 0:
			for cl in self.ARR:
				img = cl.get_img_off(self.var.get())
				sv_pth = self.dir_pth +"/OFF_" + cl.name + ".jpg"
				img.save(sv_pth)
				img = cl.get_img_on()
				sv_pth = self.dir_pth +"/ON_" + cl.name + ".jpg"
				img.save(sv_pth)


root = Tk()
root.title("Color IMG Generator")
app = GUI(root)

root.mainloop()
