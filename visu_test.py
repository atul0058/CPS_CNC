from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import pymysql

class App(threading.Thread):

    def __init__(self,tk_root):
        self.root = tk_root
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        print("Starting....")
        
my_window = Tk()

conn = pymysql.connect(host="localhost", user="root", passwd="raspberry", db="CNC")
cur = conn.cursor()

label  = [[0 for i in range(13)] for i in range(13)]
for i in range(12):
    for j in range(12):
        label[i][j] = Label( my_window, width = '10', height = '3', bg = 'white')

label[0][0]=Label(my_window,width = '20', height = '3',text="Machining Stage",bd=10,bg = 'white',anchor='w')
label[1][0]=Label(my_window,width = '20', height = '3',text="Basic Module",bd=10,bg = 'white',anchor='w')
label[2][0]=Label(my_window,width = '20', height = '3',text="Coolant Pump",bd=10,bg = 'white',anchor='w')
label[3][0]=Label(my_window,width = '20', height = '3',text="Spindle Motor", bd=10,bg = 'white',anchor='w')
label[4][0]=Label(my_window,width = '20', height = '3',text="X-Axis Motor", bd=10,bg = 'white',anchor='w')
label[5][0]=Label(my_window,width = '20', height = '3',text="Y-Axis Motor", bd=10,bg = 'white',anchor='w')
label[6][0]=Label(my_window,width = '20', height = '3',text="Z-Axis Motor", bd=10,bg = 'white',anchor='w')
label[7][0]=Label(my_window,width = '20', height = '3',text="Tool Select Motor",bd=10,bg = 'white',anchor='w')
label[8][0]=Label(my_window,width = '20', height = '3',text="Tool Change Motor",bd=10,bg = 'white',anchor='w')
label[9][0]=Label(my_window,width = '20', height = '3',text="Cutting Operation",bd=10,bg = 'white',anchor='w')

label[0][0].grid(row=0,column=0)
label[1][0].grid(row=1,column=0)
label[2][0].grid(row=2,column=0)
label[3][0].grid(row=3,column=0)
label[4][0].grid(row=4,column=0)
label[5][0].grid(row=5,column=0)
label[6][0].grid(row=6,column=0)
label[7][0].grid(row=7,column=0)
label[8][0].grid(row=8,column=0)
label[9][0].grid(row=9,column=0)

def show_info():
    query="select Power_W,Time_sec from test2"
    cur.execute(query)
    result=cur.fetchall()
    cur.close()
    x=[]
    y=[]
    for i in range(len(result)):
            y.append(result[i][0])
            x.append(result[i][1])
    x1 = [p for p in x ]  
    y1 = [p for p in y] 
    fig=Figure(figsize=(5,4),dpi=100)
    ax=fig.add_subplot(111).plot(x1,y1)
    fig.text(0.5, 0.03, 'Time (seconds)', ha='center', va='center')
    fig.text(0.04, 0.5, 'Power (W)', ha='center', va='center', rotation='vertical')
    canvas=FigureCanvasTkAgg(fig,master=my_window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0,column=6,rowspan=6)



APP = App(my_window)
my_window.after(1000,show_info)
my_window.geometry("1800x800+0+0")
my_window.title("CPS of CNC")
my_window['bg']='white'
my_window.mainloop()
