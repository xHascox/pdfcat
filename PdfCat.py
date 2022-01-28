from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory
from tkinter.filedialog import asksaveasfilename
import tkinter.scrolledtext as scrolledtext
from PyPDF2 import PdfFileMerger
import time

pdf2_path = ""
pdf1_path = ""

def pufile(msg="choose a file"):
    '''
    tkinter GUI: Prompts the User to choose one Files
    Returns a string of the file-path
    '''
    from tkinter.filedialog import askopenfilename
    name = askopenfilename(initialdir=".",
                           filetypes =(("All Files","*.*"),),
                           title = msg
                           )
    try:
        return name
    except:
        return False

def run(pdf1, pdf2):
    merger = PdfFileMerger()
    merger.append(pdf1)
    merger.append(pdf2)
    merger.write(".\\PdfCat_"+str(time.time())+".pdf")
    merger.close()

def get_pdf1():
    pdf1_path = pufile("choose first pdf file")
    pdf2_path = pufile("choose second pdf file")
    print(pdf1_path)
    run(pdf1_path, pdf2_path)

    



#GUI
root=Tk()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.place(fill=BOTH, expand=1)

#BUTTONS
row=Frame(root)
row.pack(side=TOP, padx=10, pady=10, fill=X)
descr=Label(row, text="PDF Files to concatenate", font=("Helvetica", 12), anchor=W, justify=LEFT)#width=15
pdf1 = Button(row, text="Dateien wählen", command=get_pdf1)
descr.pack(side=LEFT, padx=10, pady=10)
pdf1.pack(side=RIGHT,padx=10, pady=10)







root.wm_title("PdfCat")
root.geometry("600x400")#wxh
root.update()
root.mainloop()