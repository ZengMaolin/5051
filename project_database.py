import time
import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class traffic_data_show():
    def __init__(self):
        # This dict for plotting part text show
        self.car_dic = {
            5:'Contact Car',
            31:'Small Passenger Car',
            32:'Small Truck',
            41:'Bus',
            42:'Big Truck'
        }
        self.velcles = []

        self.traffic_data = self._read()
        # This 5 type data is for details show
        self.v_5_data = self.traffic_data[self.traffic_data['VehicleType'] == 5] 
        self.v_31_data = self.traffic_data[self.traffic_data['VehicleType'] == 31] 
        self.v_32_data = self.traffic_data[self.traffic_data['VehicleType'] == 32] 
        self.v_41_data = self.traffic_data[self.traffic_data['VehicleType'] == 41] 
        self.v_42_data = self.traffic_data[self.traffic_data['VehicleType'] == 42] 
        
        # This 5 type data is for plotting
        self.v_5_hist_data,self.v_5_hist_bins = self._get_plot_data(5)
        self.v_31_hist_data,self.v_31_hist_bins = self._get_plot_data(31)
        self.v_32_hist_data,self.v_32_hist_bins = self._get_plot_data(32)
        self.v_41_hist_data,self.v_41_hist_bins = self._get_plot_data(41)
        self.v_42_hist_data,self.v_42_hist_bins = self._get_plot_data(42)
        
        # This one is for pie plotting
        self.car_distribution_num = self.traffic_data.groupby(['VehicleType'])['TripEnd'].count()
        
    def _read(self):
        tmp = pd.read_csv("TDCS_M06A_20190830_080000.csv", header=None)
        tmp.columns = ['VehicleType','DerectionTime_O','Gantry_O','DerectionTime_D','Gantry_D','TripLength','TripEnd','TripInfo']
        return tmp
        
    def _show_head(self):
        print(self.traffic_data.head())

    def _vtype_converge(self,vtype):
        if vtype == 5:return self.v_5_data
        elif vtype == 31:return self.v_31_data
        elif vtype == 32:return self.v_32_data
        elif vtype == 41:return self.v_41_data
        elif vtype == 42:return self.v_42_data
        
    def _get_plot_data(self,vtype):
        tmp = self._vtype_converge(5)
        tmp = tmp[['TripLength']]
        data = tmp.values.reshape(-1)
        bins = np.linspace(0,max(data),51)
        return data,bins
    
    def _grasp_plot_data(self,vtype):
        if vtype == 5:return self.v_5_hist_data,self.v_5_hist_bins
        elif vtype == 31:return self.v_31_hist_data,self.v_31_hist_bins
        elif vtype == 32:return self.v_32_hist_data,self.v_32_hist_bins
        elif vtype == 41:return self.v_41_hist_data,self.v_41_hist_bins
        elif vtype == 42:return self.v_42_hist_data,self.v_42_hist_bins
        
        
        
        
    # page1 :agg func 
    
    def car_distribution(self):
        num = self.car_distribution_num
        values = num.values
        text = ['Contact Car','Small Passenger Car','Small Truck','Bus','Big Truck']
        colors = ['g','b','r','c','m']
        plt.pie(values,
#               labels=text,
              autopct = '%3.2f%%',
              colors = colors,
              shadow = False, 
              startangle =90, 
              pctdistance = 1.1,
              labeldistance = 1
               ) 
        for i in range(len(text)):
            plt.plot([],[],label = text[i],color = colors[i],linewidth=5)
        plt.legend(loc = (0.89,0.4),handlelength = 0.2)
        plt.axis('equal')
        plt.title('The Proportion of 5 type Vehicle',fontsize=15,x=0.8,y=1.13)
        plt.show()
    
    
    
    

        
    # page2 :details func
    def earliest_details(self,vtype):
        tmp = self._vtype_converge(vtype) # self.traffic_data[self.traffic_data['VehicleType'] == vtype]
        df = tmp.sort_values(by=['DerectionTime_O'])
        output = df.head(10)
        print(output.to_string(index=False))
    
    def latest_details(self,vtype):
        tmp = self._vtype_converge(vtype) # self.traffic_data[self.traffic_data['VehicleType'] == vtype]
        df = tmp.sort_values(by=['DerectionTime_O'],ascending=False)
        output = df.head(10)
        print(output.to_string(index=False))
    
    
    def shortest_distance_details(self,vtype):
        tmp = self._vtype_converge(vtype) # tmp = self.traffic_data[self.traffic_data['VehicleType'] == vtype]
        df = tmp.sort_values(by=['TripLength'])
        output = df.head(10)
        print(output.to_string(index=False))
        
        
    def longest_distance_details(self,vtype):
        tmp = self._vtype_converge(vtype) #tmp = self.traffic_data[self.traffic_data['VehicleType'] == vtype]
        df = tmp.sort_values(by=['TripLength'],ascending=False)
        output = df.head(10)
        print(output.to_string(index=False))
    
    
    def distance_hist(self,vtype):
        data,bins = self._grasp_plot_data(vtype)
        plt.figure(figsize=(8,5), dpi=100) 
        plt.hist(data, bins, histtype='bar', rwidth=1,color="steelblue",edgecolor="black",density=True,label="hist")

        plt.xlim(-10,1000)
        plt.xlabel("TripLength")
        plt.ylabel("probability")
        plt.title("TripLength's Probability Distribution of {}".format( self.car_dic[vtype]))
        plt.legend()
        plt.show()
    
    
    
def init_():
    
    return class
    
    class.gui_inerface(1)

    
            
if __name__ == '__main__':
    a  = traffic_data_show()
#     a.earliest_details(31)
#     a.shortest_distance_details(31)
    a.car_distribution()
#     a.distance_hist(42)




class fac():
    def get_()：
        return 0



class high_way():
    def __init__(self) -> None:
        fac = fac()
        self.velcles = []

    def add_velcles():
        self.velcles
        pass
class high_way_show():
    ..
    ..
    ...
    ...

    #inter face
    def gui_interface(command):
        # command :1 get ..

        pass



main():
#init
    init()