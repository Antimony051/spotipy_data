def plotter(inparr):
    axis_x=[a for a in range(len(inparr))]
    axis_y=inparr
    plt.plot(axis_x, axis_y)
    plt.show()

def find_total_time():
    total=0
    for x in json_data():
        time=x["ms_played"]
        total+=time
    return (total//60000)        # return the value in minutes

def no_of_songs_by_time(time_zone=0,resolution=5):
    time_diff=time_zone//resolution
    no_slots=1440//resolution                       #number_of_slots
    timarr=[0]*(no_slots)                           # an array containing required number of zeros, each represents a block corresponding to the resolution, default res is 5 mins
    for x in json_data:
        minutes_=int(x["ts"][-6:-4])                # extract the minute
        hours_=int(x["ts"][-9:-7])                  # extract the hour
        minute=(hours_*60+minutes_)//resolution     # converting them into minutes and packing them into chunks of 5 min
        timarr[(minute+time_diff)%no_slots]+=1      # correct the time zone and increment teh corresponding time slot 
                                                    #to do, rotate the list at the end instead of doing math
    plotter(timarr)

def song_by_month():
    montharr=[0]*12
    for x in range(len(json_data)):
        month=int(json_data[x]["endTime"][5:7])
        montharr[month-1]+=1
    plotter(montharr)

def json_handler(f_name):
    current_file= open(f_name)
    json_data=json.load(current_file)
    current_file.close()

# to do songs by date: your first song etc

class get_all():
    dict={}
    def __init__(self,feild_name):
        self.field=feild_name
        for x in json_data:
            element=x[self.field]
            if element in self.dict:
                self.dict[element]+=1
            else:
                self.dict[element]=1
    def top_10(self):
        self.sorted_list=sorted(a.items(), key=lambda x:x[1],reverse=True)
        return self.sorted_list[:10]
