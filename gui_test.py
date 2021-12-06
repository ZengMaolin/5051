import tkinter as tk
from project_database_v2 import init as db_init
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import math



def car_distribution(ax, values, explode_index:int):      
     text = ['Contact Car','Small Passenger Car','Small Truck','Bus','Big Truck']
     colors = ['g','b','r','c','m']
     explode = [0,0,0,0,0]
     if explode_index < 5:
          explode[explode_index] = 0.1
     ax.pie(values,
          #   labels=text,
               autopct = '%3.2f%%',
               colors = colors,
               shadow = True, 
               startangle =0, 
               pctdistance = 1.2,
               labeldistance = 1,
               explode=explode,
          ) 
     for i in range(len(text)):
          ax.plot([],[],label = text[i],color = colors[i],linewidth=5)

     ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.1), frameon=False)
     if explode_index < 5:
          ax.set_title('You are choosing:'+text[explode_index])
     else: 
          ax.set_title('Please selet')

     ax.axis('equal')

last_position =  100

def motion(event):
     global last_position
     x, y = event.x, event.y
     if  ((x-420)**2 + (y-320)**2) > 53000:
          canvas.config(cursor='arrow')
          return
     canvas.config(cursor='hand')
     #calculate the center 420/320
     if x != 420:
          if x < 420:
               theta = math.atan((320-y)/(x-420)) + math.pi
          else:
               theta = math.atan((320-y)/(x-420)) 
               if theta < 0:
                    theta += math.pi * 2
          if theta < math.pi * 2 * 0.042:
               current_postion = 0
          elif theta < math.pi * 2 * 0.69:
               current_postion = 1
          elif theta < math.pi * 2 * 0.93:
               current_postion = 2
          elif theta < math.pi * 2 * 0.945:
               current_postion = 3
          else: 
               current_postion = 4
          if current_postion != last_position:
               last_position = current_postion
               fig_main.clear()
               car_distribution(fig_main.gca(),values,current_postion)
               fig1.draw()

def createNewWindow(x):
    newWindow = tk.Toplevel(root)
    labelExample = tk.Label(newWindow, text = f"New Window {x}")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()


def mouse_clicked(event):
     global last_position
     x, y = event.x, event.y
     if  ((x-420)**2 + (y-320)**2) > 53000:
          return
     #calculate the center 420/320
     if x != 420:
          if x < 420:
               theta = math.atan((320-y)/(x-420)) + math.pi
          else:
               theta = math.atan((320-y)/(x-420)) 
               if theta < 0:
                    theta += math.pi * 2
          if theta < math.pi * 2 * 0.042:
               current_postion = 0
          elif theta < math.pi * 2 * 0.69:
               current_postion = 1
          elif theta < math.pi * 2 * 0.93:
               current_postion = 2
          elif theta < math.pi * 2 * 0.945:
               current_postion = 3
          else: 
               current_postion = 4
     print(current_postion)
     if current_postion != last_position:
               last_position = current_postion
               fig_main.clear()
               car_distribution(fig_main.gca(),values,current_postion)
               fig1.draw()
     createNewWindow(current_postion)


root = tk.Tk()
root.geometry('800x800')
root.maxsize(800,800)
root.minsize(800,800)
root.title('5051 final project')
label_title = tk.Label(root,text='Inquiry system for Taiwan traffic data',font=('',40))
label_title.place(relx=0.18,rely=0)

data_inter_face = db_init()
values = data_inter_face.gui_interface(0)
fig_main = plt.figure(figsize=(8, 6), dpi=70)
car_distribution(fig_main.gca(),values,7)
canvas = tk.Canvas(root,cursor='hand',width=790, height=600, bg='white')
fig1 = FigureCanvasTkAgg(fig_main, master=canvas)
fig1.draw()
fig1.get_tk_widget().place(x=0,y=0)
fig1.get_tk_widget().bind('<Motion>', motion)
fig1.get_tk_widget().bind("<Button-1>", mouse_clicked)

canvas.place(x=5,y=100)


root.mainloop()