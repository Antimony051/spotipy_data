import os
import json
import re
"""
the purpose of this module is to combine all the relevant json files into a single file
while combining them it gets rid of fields that are not needed
for example the key 'platform' is not included into the output file
"""
# every key in the original file = ['ts','username','platform','ms_played','conn_country','ip_addr_decrypted','user_agent_decrypted','master_metadata_track_name','master_metadata_album_artist_name','master_metadata_album_album_name','spotify_track_uri','episode_name','episode_show_name','spotify_episode_uri','reason_start','reason_end','shuffle','skipped','offline','offline_timestamp','incognito_mode']
arr=['ts','ms_played','master_metadata_track_name','master_metadata_album_artist_name','master_metadata_album_album_name']    # all the keys that we need

def mange_files(path_input=None,out_file_name="processed.json"):
    total_files_processed=0

    def setup_out_file(path_,chr_to_write,mode="a"):
        out_file=open(f"{path_}/{out_file_name}",mode)
        out_file.write(chr_to_write)
        out_file.close()

    def remove_chars(path_,num_to_remove):
        out_file=open(f"{path_}/{out_file_name}","rb+")
        out_file.seek(0,2)
        size=out_file.tell()
        out_file.truncate(size-num_to_remove)

    def process_file(folder,f_name):               # the original json file contains 21 differnt keys, we don't need all of them
        current_file= open(f_name)                 # we read the file and write only the relvelent content to out file 
        json_data=json.load(current_file)
        current_file.close()
        with open(f"{folder}/{out_file_name}","a") as out_file:
            for x in json_data:
                out_file.write("{")
                for key in arr[:-1]:  
                    value=json.dumps(x[key])        # using json.dumps is necessay becuase it escapes " and \ present in the string x[key]
                    out_file.write(f'"{key}":{value},')
                out_file.write(f'"{arr[-1]}":{json.dumps(x[arr[-1]])}')       # the last one is handled out of loop because we don't want a comma after it
                out_file.write("},\n")

    if path_input:
        path_=path_input
        print(f"looking for your file in {path_input}\n")
    else:
        path_=os.getcwd()
        print(f"looking for your file in {os.getcwd()}\n")

    list_of_files=os.listdir(path_)                 # get a list of all files in the given directory
    
    setup_out_file(path_,'[',"w")                     # initilise the file with '['

    for file_name in list_of_files:
        is_useful_file=bool(re.search('20\d\d_\d+\.json',file_name)) # check if the file name is in format [some date beginning form 2000]_[any number from 0 to inf].json
        if is_useful_file:
            print(f"processing {file_name} now.")
            path_to_file=path_+"/"+file_name
            process_file(path_,path_to_file)       #call the function
            total_files_processed+=1

    remove_chars(path_,2)                          # need to remove the 2 charcters ',' and the new line character
    setup_out_file(path_,']')                      # end the file with ']'

    if total_files_processed==0:
        print("NO FILES PROCESSED!\n make sure the path you entered is correct.")
    else:
        print(f"sucessfully processed {total_files_processed} files!") 
    return(f"{path_}/{out_file_name}")
