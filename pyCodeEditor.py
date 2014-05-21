#!/usr/bin/python
import Tkinter as tk

class pyCodeEditor(tk.Frame):

    def __init__(self, master=0):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        #Findind the "TOP" element to make resizeble
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        #Only the second (1) column will be resizeble. The first will contain only the line numbers
        top.columnconfigure(1, weight=1)

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(0,weight=10)

        #Creating the left bar to show the line numbers
        self.canvas = tk.Canvas(bg='#E4E4E4')
        self.canvas.grid(row=0,column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.lineNumber = tk.Label(self.canvas, text='10')
        self.lineNumber.grid(row=0, column=0)

        #The component to input the text
        self.textArea = tk.Text()
        self.textArea.grid(row=0,column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        #The Y Scrollbar
        self.yScrollBar = tk.Scrollbar(command=self.textArea.yview)
        self.yScrollBar.grid(row=0,column=3, sticky=tk.N+tk.S+tk.E+tk.W)

        #The X Scrollbar
        self.xScrollBar = tk.Scrollbar(command=self.textArea.xview)
        self.xScrollBar.grid(row=1,column=0, orientation=tk.HORIZONTAL,sticky=tk.N+tk.S+tk.E+tk.W)

        self.textArea['yscrollcommand'] = self.yScrollBar.set
        self.textArea['xscrollcommand'] = self.xScrollBar.set
        

App = pyCodeEditor()
App.master.title('PyCodeEditor')
App.mainloop()
