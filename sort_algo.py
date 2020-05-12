from tkinter import *
import sys
import random
from bubble_sort import bub_sort
from merge_sort import mergeSort,merge
from insertion_sort import insertionSort
from quick_sort import partition, quickSort

root = Tk()
root.title("Sorting Algorithm visualisation")
root.config(bg="gray85")

def drawdata(data,color):
    c.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [i / (max(data)) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i*x_width + offset + spacing
        y0 = c_height - height*340

        x1 = (i+1)*x_width + offset
        y1 = c_height

        c.create_rectangle(x0, y0, x1, y1, fill=color[i])
        c.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()

def generate():
    global data
    minEntry = int(min_val.get())
    maxEntry = int(max_val.get())
    size = int(data_size.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minEntry, maxEntry+1))

    drawdata(data, ['red' for x in range(len(data))])

def start():
    global data

    if var.get() == OptionList[0]:
        bub_sort(data,drawdata,speed.get())
    if var.get() == OptionList[1]:
        mergeSort(data,0,int(data_size.get()) - 1,drawdata,speed.get())
    if var.get() == OptionList[2]:
        insertionSort(data,drawdata,speed.get())
    if var.get() == OptionList[3]:
        quickSort(data,0,int(data_size.get()) - 1,drawdata,speed.get())

def stop():
    sys.exit('stopped')

# the UI frame
frame = Frame(root, width=600, height=200, bg="dark sea green")
frame.grid(row=0,column=0,padx=10,pady=5)

c = Canvas(root, height=400, width=600, bg="gray78")
c.grid(row=1,column=0, padx=5, pady=5)

# Row 0
min_val = Scale(frame,from_=0, to=10,length=100,resolution=1,orient=HORIZONTAL,label="Min. value",activebackground="lavender")
min_val.grid(row=0,column=0,padx=5,pady=5)
min_val.config(bg="LightCyan2")

max_val = Scale(frame,from_=80, to=100,length=100,resolution=1,orient=HORIZONTAL,label="Max. value",activebackground="lavender")
max_val.grid(row=0,column=1,padx=5,pady=5)
max_val.config(bg="LightCyan2")

speed = Scale(frame, from_=0.001, to=0.5,length=100,digits=3,resolution=0.005,orient=HORIZONTAL,label="Select speed[s]",activebackground="lavender")
speed.grid(row=0,column=2,padx=5,pady=5)
speed.config(bg="LightCyan2")

data_size = Scale(frame, from_=0, to=100,length=100,resolution=1,orient=HORIZONTAL,label="Data size",activebackground="lavender")
data_size.grid(row=0,column=3,padx=5,pady=5)
data_size.config(bg="LightCyan2")

# row 1
l = Label(frame,text="Algorithms",font="Helvetica")
l.grid(row=1,column=0)

OptionList = [
"bubble sort",
"merge sort",
"insertion sort",
"quick sort"
]

var = StringVar(root)
var.set(OptionList[0])

opt = OptionMenu(frame, var, *OptionList)
opt.config(width=20, font=('Helvetica', 12))
opt.grid(row=1,column=1,padx=5,pady=5)

btn1 = Button(frame,text="Generate",command=generate,bg="OliveDrab2",activebackground="OliveDrab1")
btn1.grid(row=1,column=2,padx=5,pady=5)

btn2 = Button(frame,text="Start",command=start,bg="lime green",activebackground="forest green")
btn2.grid(row=1,column=3,padx=5,pady=5)

btn3 = Button(frame,text="Exit",command=stop,bg="red3",activebackground="red4")
btn3.grid(row=1,column=4,padx=5,pady=5)

root.mainloop()
