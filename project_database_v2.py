import time
import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#  ｢高速公路電子收費交通資料蒐集支援系統(TDCS, Traffic Data Collection System)


class Database():
    def __init__(self):
        self.traffic_data = self._read()
        
    def _read(self):
        tmp = pd.read_csv("TDCS_M06A_20190830_080000.csv", header=None)
        tmp.columns = ['VehicleType','DerectionTime_O','Gantry_O','DerectionTime_D','Gantry_D','TripLength','TripEnd','TripInfo']
        return tmp
    
class DataProcessing():
    def __init__(self,data,hist_data,hist_bins):
        self.data = data # DataFrame for details show
        self.hist_data = hist_data
        self.hist_bins = hist_bins  # List for plotting
        
class VehicleDataFactory():
    def __init__(self):
        self.db = Database()
        
    def get_vehicle_data(self,vtype = 5):
        if vtype in [5,31,32,41,42]:
            data = self.db.traffic_data[self.db.traffic_data['VehicleType'] == vtype]
            hist_data,hist_bins = self._get_plot_data(vtype)
            return DataProcessing(data,hist_data,hist_bins)

    def _get_plot_data(self,vtype):
        tmp = self.db.traffic_data[self.db.traffic_data['VehicleType'] == vtype]
        tmp = tmp[['TripLength']]
        data = tmp.values.reshape(-1)
        bins = np.linspace(0,max(data),51)
        return data,bins

class TDCS():
    def __init__(self):
        self.vehicle = []
        self._vehicle_filling()
    
    def _vehicle_filling(self):
        factory = VehicleDataFactory()
        for i in [5,31,32,41,42]:
            self.vehicle.append(factory.get_vehicle_data(i))
    
    def get_vehicle(self):
        return self.vehicle

class TDCS_PlottingShow(TDCS):
    def __init__(self):
        super().__init__()
        self.car_dic = {
            5:'Contact Car',
            31:'Small Passenger Car',
            32:'Small Truck',
            41:'Bus',
            42:'Big Truck'
        }
        self.car_distribution_num = self._organize_total_data()
        
    def _organize_total_data(self):
        df = pd.DataFrame()
        for i in self.vehicle:
            df = pd.concat([df,i.data],ignore_index = True)
        return df.groupby(['VehicleType'])['TripEnd'].count()
    
    def _grasp_plot_data(self,vtype):
        if vtype == 5:return self.vehicle[0].hist_data,self.vehicle[0].hist_bins
        elif vtype == 31:return self.vehicle[1].hist_data,self.vehicle[1].hist_bins
        elif vtype == 32:return self.vehicle[2].hist_data,self.vehicle[2].hist_bins
        elif vtype == 41:return self.vehicle[3].hist_data,self.vehicle[3].hist_bins
        elif vtype == 42:return self.vehicle[4].hist_data,self.vehicle[4].hist_bins
    
    def car_distribution(self):
        num = self.car_distribution_num
        values = num.values
        return values
        # text = ['Contact Car','Small Passenger Car','Small Truck','Bus','Big Truck']
        # colors = ['g','b','r','c','m']
        # fig = plt.figure(figsize=(8, 6), dpi=70)
        # explode = (0, 0.1, 0, 0, 0)
        # plt.pie(values,
        #     #   labels=text,
        #         autopct = '%3.2f%%',
        #         colors = colors,
        #         shadow = False, 
        #         startangle =90, 
        #         pctdistance = 1.2,
        #         labeldistance = 1,
        #         explode=explode,
        #        ) 
        # for i in range(len(text)):
        #     plt.plot([],[],label = text[i],color = colors[i],linewidth=5)
        # plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1), frameon=False)
        # plt.axis('equal')
        # # plt.title('The Proportion of 5 type Vehicle',fontsize=12)

        # return fig

        
    
    
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
        
        
class TDCS_DetailsShow(TDCS):
    def __init__(self):
        super().__init__()
    def _vtype_converge(self,vtype):
        if vtype == 5:return self.vehicle[0].data
        elif vtype == 31:return self.vehicle[1].data
        elif vtype == 32:return self.vehicle[2].data
        elif vtype == 41:return self.vehicle[3].data
        elif vtype == 42:return self.vehicle[4].data
        
    def earliest_details(self,vtype):
        tmp = self._vtype_converge(vtype)[['DerectionTime_O']]
        df = tmp.sort_values(by=['DerectionTime_O'])
        output = df.head(10)
        print(output.to_string(index=False))
    
    def latest_details(self,vtype):
        tmp = self._vtype_converge(vtype)[['DerectionTime_O']]
        df = tmp.sort_values(by=['DerectionTime_O'],ascending=False)
        output = df.head(10)
        print(output.to_string(index=False))
    
    
    def shortest_distance_details(self,vtype):
        tmp = self._vtype_converge(vtype)[['TripLength']]
        df = tmp.sort_values(by=['TripLength'])
        output = df.head(10)
        print(output.to_string(index=False))
        
        
    def longest_distance_details(self,vtype):
        tmp = self._vtype_converge(vtype)[['TripLength']]
        df = tmp.sort_values(by=['TripLength'],ascending=False)
        output = df.head(10)
        return output.to_string(index=False)
    
    

class GuiInterface():
    def __init__(self):
        self.plotting = TDCS_PlottingShow()
        self.details = TDCS_DetailsShow()
        
    def gui_interface(self,output_type = 0):
        # output_type dict
        # 0 : Call car distribution
        
        # 50 : Call Contact Car trip length distribution
        # 51 : Call Contact Car earliest details
        # 52 : Call Contact Car latest details
        # 53 : Call Contact Car shortest distance details
        # 54 : Call Contact Car longest distance details
        
        # 310 : Call Small Passenger Car trip length distribution
        # 311 : Call Small Passenger Car earliest details
        # 312 : Call Small Passenger Car latest details
        # 313 : Call Small Passenger Car shortest distance details
        # 314 : Call Small Passenger Car longest distance details
        
        # 320 : Call Small Truck trip length distribution
        # 321 : Call Small Truck earliest details
        # 322 : Call Small Truck latest details
        # 323 : Call Small Truck shortest distance details
        # 324 : Call Small Truck longest distance details  
        
        # 410 : Call Bus trip length distribution
        # 411 : Call Bus earliest details
        # 412 : Call Bus latest details
        # 413 : Call Bus shortest distance details
        # 414 : Call Bus longest distance details  
        
        # 420 : Call Big Truck trip length distribution
        # 421 : Call Big Truck earliest details
        # 422 : Call Big Truck latest details
        # 423 : Call Big Truck shortest distance details
        # 424 : Call Big Truck longest distance details  
        
        if output_type == 0:    return self.plotting.car_distribution()

        elif output_type == 50: return self.plotting.distance_hist(5)
        elif output_type == 51: return self.details.earliest_details(5)
        elif output_type == 52: return self.details.latest_details(5)
        elif output_type == 53: return self.details.shortest_distance_details(5)
        elif output_type == 54: return self.details.longest_distance_details(5)
        
        elif output_type == 310:return self.plotting.distance_hist(31)
        elif output_type == 311:return self.details.earliest_details(31)
        elif output_type == 312:return self.details.latest_details(31)
        elif output_type == 313:return self.details.shortest_distance_details(31)
        elif output_type == 314:return self.details.longest_distance_details(31)

        elif output_type == 320:return self.plotting.distance_hist(32)
        elif output_type == 321:return self.details.earliest_details(32)
        elif output_type == 322:return self.details.latest_details(32)
        elif output_type == 323:return self.details.shortest_distance_details(32)
        elif output_type == 324:return self.details.longest_distance_details(32)
            
        elif output_type == 410:return self.plotting.distance_hist(41)
        elif output_type == 411:return self.details.earliest_details(41)
        elif output_type == 412:return self.details.latest_details(41)
        elif output_type == 413:return self.details.shortest_distance_details(41)
        elif output_type == 414:return self.details.longest_distance_details(41)
            
        elif output_type == 420:return self.plotting.distance_hist(42)
        elif output_type == 421:return self.details.earliest_details(42)
        elif output_type == 422:return self.details.latest_details(42)
        elif output_type == 423:return self.details.shortest_distance_details(42)
        elif output_type == 424:return self.details.longest_distance_details(42)  

def init():
    return GuiInterface()
    
if __name__ == '__main__':
    ob = init()
    while True:
        x = int(input("input command"))
        ob.gui_interface(x)



    