import matplotlib.pyplot as plt
import numpy as np
from datetime import date
def setup_plt():
    plt.style.use("seaborn")
    cmap=plt.get_cmap("BuPu")
    return(cmap([0.97,0.94,0.91,0.88,0.85,0.82,0.79,0.76,0.73,0.7]))
    
def plotter(axis_x,axis_y):
    # axis_x=[a for a in range(len(inparr))]
    # axis_y=inparr
    setup_plt()
    plt.plot(axis_x,axis_y,color="darkturquoise")
    plt.title('number of songs played as a function of time')
    plt.xlabel("time")
    plt.ylabel("number of songs")
    plt.show()

def bar_chart_drawer(values,title_name="title",x_lable="x",y_lable="y"):
    x_axis_val=[]
    y_axis_val=[]
    for x in values:
        x_axis_val.append(x[0][:10])
        y_axis_val.append(x[1])

    colour_=setup_plt()
    plt.bar(x_axis_val,y_axis_val,color=colour_)
    plt.title(title_name)
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.xticks(rotation = 45)
    plt.show()

def find_total_time(json_data):
    total=0
    for x in json_data():
        time=x["ms_played"]
        total+=time
    return (total//60000)        # return the value in minutes

def no_of_songs_by_time(json_data,time_zone=0,smoothness=5):
    time_diff=time_zone//smoothness                 # rounding to -inf might cause slight inaccuracies when time zone is negative 
    no_slots=1440//smoothness                       #number_of_slots
    no_songs=[0]*(no_slots)                           # an array containing required number of zeros,each represents a block corresponding to the smoothness,default res is 5 mins
    for x in json_data:
        minutes_=int(x["ts"][-6:-4])                # extract the minute
        hours_=int(x["ts"][-9:-7])                  # extract the hour
        minute=(hours_*60+minutes_)//smoothness     # converting them into minutes and packing them into chunks of 5 min
        no_songs[(minute+time_diff)%no_slots]+=1      # correct the time zone and increment the corresponding time slot 
                                                    #to do,rotate the list at the end instead of doing math
    hour_list=np.linspace(0,23.9,len(no_songs))
    plotter(hour_list,no_songs)

def song_by_month(json_data):
    montharr=[]
    prev=None
    for x in json_data:
        month=int(x["ts"][5:7])     # extract the month from the date
        if prev==month:             # if month has not changed
            montharr[-1]+=1         # increment the same month
        else:
            montharr.append(1)      # add new element to the list
            prev=month              # update prev
    
    first_date=json_data[0]["ts"][:7]
    last_date=json_data[-1]["ts"][:7]
    times = np.arange(np.datetime64(first_date),
                  np.datetime64(last_date), 
                  np.timedelta64(1, 'M'))
    plotter(times,montharr[:len(times)])
    # todo, len(montharr) will be less than len(times) if user has not listned to any songs in atlest one month. we can fix this by adding required 0's in  montharr


def first_10_songs(json_data):
    arr=[]
    c=0
    for x in json_data:
        arr.append(x["master_metadata_track_name"])

def songs_per_week(json_data):
    pass
# to do songs by date: your first song etc
# your top 10 songs tracked through time
class get_all():

    def __init__(self,feild_name,json_data):
        self.dict={}
        self.field=feild_name
        for x in json_data:
            element=x[self.field]
            if element in self.dict:
                self.dict[element]+=1
            else:
                self.dict[element]=1
    def top_10(self):
        self.sorted_list=sorted(self.dict.items(),key=lambda x:x[1],reverse=True)
        return self.sorted_list[:10]
