import tkinter as tk

from matplotlib import colors
from project_database_v2 import init as db_init
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import math


class main_page:
     def __init__(self, main_widow) -> None:
          self.main_window = main_widow
          self.main_window.geometry('800x800')
          self.main_window.maxsize(800,800)
          self.main_window.minsize(800,800)
          self.main_window.title('5051 final project, design by Maolin, Jinhuai and Yanyan')
          self.label_title = tk.Label(self.main_window, text='Inquiry system for Taiwan traffic data', font=('',40))
          self.label_title.place(relx=0.1,rely=0)

          self.data_inter_face = db_init()
          self.values_car_distribution = self.data_inter_face.gui_interface(0)
          self.fig_main = plt.figure(figsize=(8, 6), dpi=70)
          self.car_distribution(self.fig_main.gca(),7)
          self.canvas = tk.Canvas(self.main_window, cursor='hand', width=790, height=600, bg='white')
          self.fig1 = FigureCanvasTkAgg(self.fig_main, master=self.canvas)
          self.fig1.draw()
          self.fig1.get_tk_widget().place(x=0,y=0)
          self.fig1.get_tk_widget().bind('<Motion>', self.motion)
          self.fig1.get_tk_widget().bind("<Button-1>", self.mouse_clicked)
          self.canvas.place(x=5,y=100)
          self.last_position =  100
          self.buttton_show_all = tk.Button(self.main_window, text="Show all data", width=12, height=2, font=('',25), borderwidth=5, relief='groove')
          self.buttton_show_all.place(x=550,y=725)
          self.label_cars = tk.Label(self.main_window, text=f'Totlal {sum(self.values_car_distribution)} cars with 5 Types', font=('',25), fg='blue')
          self.label_cars.place(relx=0.3,y=50)
          self.car_window_dict = {}

     def car_distribution(self, ax, explode_index:int):      
          text = ['Contact Car','Small Passenger Car','Small Truck','Bus','Big Truck']
          colors = ['g','b','r','c','m']
          explode = [0,0,0,0,0]
          if explode_index < 5:
               explode[explode_index] = 0.1
          ax.pie(self.values_car_distribution,
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
               ax.set_title('You are choosing:'+text[explode_index]+f'\ntotal: {self.values_car_distribution[explode_index]}')
          else: 
               ax.set_title('Please selet')

          ax.axis('equal')

     

     def motion(self, event):
          x, y = event.x, event.y
          if  ((x-420)**2 + (y-320)**2) > 53000:
               self.canvas.config(cursor='arrow')
               return
          self.canvas.config(cursor='hand')
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
               if current_postion != self.last_position:
                    self.last_position = current_postion
                    self.fig_main.clear()
                    self.car_distribution(self.fig_main.gca(), current_postion)
                    self.fig1.draw()

     def createNewWindow(self, x):
          if x not in self.car_window_dict:
               newWindow = tk.Toplevel(self.main_window)
               labelExample = tk.Label_title(newWindow, text = f"New Window {x}")
               buttonExample = tk.Button(newWindow, text = "New Window button")

               labelExample.pack()
               buttonExample.pack()
               self.car_window_dict[x] = newWindow




     def mouse_clicked(self, event):
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
          if current_postion != self.last_position:
                    self.last_position = current_postion
                    self.fig_main.clear()
                    self.car_distribution(self.fig_main.gca(), current_postion)
                    self.fig1.draw()
          self.createNewWindow(current_postion)


root = tk.Tk()
main_gui = main_page(root)
root.mainloop()