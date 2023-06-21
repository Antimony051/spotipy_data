import json
import fmanager
import utils

path_input=input("enter the path to extracted Mydata file: ")
out_file_path=fmanager.mange_files(path_input)

def json_handler(f_name):
    current_file= open(f_name)
    return(json.load(current_file))
    current_file.close()

json_data=json_handler(out_file_path)

artists= utils.get_all("master_metadata_album_artist_name",json_data)
songs= utils.get_all("master_metadata_track_name",json_data)
albums= utils.get_all("master_metadata_album_album_name",json_data)

print(songs.top_10())
print(len(songs.dict))
utils.no_of_songs_by_time(json_data,time_zone=345,smoothness=5)
