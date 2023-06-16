import json
import matplotlib.pyplot as plt
import os
import re
import fmanager
import utils

path_input=input("enter the path to extracted Mydata file: ")
out_file_path=fmanager.mange_files(path_input)

json_handler(out_file_path)

artists= utils.get_all("master_metadata_album_artist_name")
songs= utils.get_all("master_metadata_track_name")
albums= utils.get_all("master_metadata_track_name")
