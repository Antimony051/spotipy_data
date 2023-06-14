import json
import matplotlib.pyplot as plt
import os
import re
path_input=input("enter the path to extracted Mydata file: ")
    
def get_all_artists():
    artists_dict={}
    for x in json_data():
        artist=x["master_metadata_album_artist_name"]
        if artist in artist_dict:
            artist_dict[artist]+=1
        else:
            artist_dict[artist]=1
    return artist_dict

def get_all_songs():
    songs_dict={}
    for x in json_data():
        song=x["master_metadata_track_name"]
        if song in songs_dict:
            songs_dict[artist]+=1
        else:
            songs_dict[artist]=1
    return songs_dict

    print(sorted(songs_dict.values()))          # to print songs by the number of times they appear 
    print(len(songs_dict))                      # number of unique songs

    print(sorted(artist_dict.values()))          # to print artists by the number of times they appear 
    print(len(artist_dict))                      # number of artists

def plotter(inparr):
    axis_x=[a for a in range(len(inparr))]
    axis_y=inparr
    plt.plot(axis_x, axis_y)
    plt.show()

def get_all_album():
    album_dict={}
    for x in json_data():
        album=x["master_metadata_track_name"]
        if alubm in album_dict:
            album_dict[artist]+=1
        else:
            album_dict[artist]=1
    return album_dict

    print(sorted(album_dict.values()))          # to print album by the number of times they appear 
    print(len(album_dict))                      # number of unique album

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
    sum=0
    json_data=json.load(current_file)

    current_file.close()

    song_by_time()

if path_input:
    path_=path_input
    print(f"looking for your file in {path_input}\n")

else:
    path_=os.getcwd()
    print(f"looking for your file in {os.getcwd()}\n")

list_of_files=os.listdir(path_)
total_files_processed=0

for file_name in list_of_files:
    is_useful_file=bool(re.search('20\d\d_\d+\.json',file_name)) # check if the file name is in format [some date beginning form 2000]_[any number from 0 to inf].json
    if is_useful_file:
        print(f"processing {file_name} now.")
        path_to_file=path_+"/"+file_name
        json_handler(path_to_file)                               #call the function
        total_files_processed+=1

if total_files_processed==0:
    print("NO FILES PROCESSED!\n make sure the path you entered is correct.")
else:
    print(f"sucessfully processed {total_files_processed} files!")
