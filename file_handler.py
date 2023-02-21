"""
Created on Fri Sep  6 20:46:33 2019
file_handler.py

Handle file operations

@author: maksimekineren
"""

# LIBRARIES NEEDED
import os
import pickle 
import datetime
from prettytable import PrettyTable
myTable = PrettyTable(["Status","File Name","Flag","Time"])
#==============================================================================
# Recursively walks the directory tree
# Finds directories and files
# Also finds hidden files (starts with '.')
#==============================================================================
def search_directory_tree(root_dir, IGNORE_LIST, LOG_FILE):
    
    try:
        # hold directories and files
        directories = dict()
        
        # recursively walk to directory tree and get files
        for dirName, subdirList, fileList in os.walk(root_dir):
            
            # remove ignore list from list
            if (IGNORE_LIST):
                for ignore in IGNORE_LIST:
                    
                    # if ignore in the list
                    if (ignore in fileList):
                        fileList.remove(ignore)
                        
            directories[str(dirName)] = fileList
        
        return directories
            
    except Exception as e:
        alertlog(LOG_FILE, \
            "Error while scanning directories and files")
        


#==============================================================================
# Save dictionary of hashes
#==============================================================================
def save_dict(dictionary, file, LOG_FILE):
    
    try:
        # open the file to use to save the dictionary
        initial_scan_file = open(file, "wb")
        
        # use pickle to save the dictionary
        pickle.dump(dictionary, initial_scan_file)
        
        # close the file
        initial_scan_file.close
        
    except Exception as e:
        alertlog(LOG_FILE, \
            "Error while saving the dictionary")



#==============================================================================
# Load dictionary of hashes
#==============================================================================
def load_dict(file, LOG_FILE):
    
    try:
        # open the pickle file to load
        infile = open(file, 'rb')
        
        # use pickle to load the dictionary
        loaded_dict = pickle.load(infile)
        
        # close the file
        infile.close()

        return loaded_dict
        
    except Exception as e:
        alertlog(LOG_FILE, \
            "Error while loading the dictionary")
    
    

#==============================================================================
# Log events
#==============================================================================
def applog(log_dir, message):
    
    # get time
    currentDT = datetime.datetime.now()
    
    # log event
    file = open(log_dir, "a+")
    file.write(str(message) + \
               "," + \
               str(currentDT.strftime("%Y-%m-%d %H:%M:%S")) + \
               "\n")
    print(str(message) + \
               "," + \
               str(currentDT.strftime("%Y-%m-%d %H:%M:%S")) + \
               "\n")
    file.close

def alertlog(log_dir, message,change,rootdir):
    
    # get time
    currentDT = datetime.datetime.now()
    
    # log event
    file = open(log_dir, "a+")
    message=message+ \
               "," + \
               str(currentDT.strftime("%Y-%m-%d %H:%M:%S")+"\n")
    file.write(message)
    
    if( change == "add"):
        change+= "e"
    print("File "+change+"d")
    ls = message.split(',')
    ls[1] = ls[1][len(str(rootdir)):]
    myTable.add_row(ls)
    file.close
    
def disptable():
    print("\n\n------Summary of the Scan Session------\n")
    print(myTable)