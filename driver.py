
"""
driver.py

Recursive File Integrity Checker
Developed to be used in CTF or CCDC competitions for Blue Teaming

Creates alerts for:
        - added files
        - removed files
        - changed files

@date 09/06/2019
@version 1.0
@author Maksim Eren
"""

# import all the libraries needed
import file_handler
import hash_handler
import suspicionDetection
import logging
import time
import dictdiffer  # pip install dictdiffer
import regex
from prettytable import PrettyTable

"""
SETTINGS START
"""
# WHERE TO START THE SCAN:
# default: same place as where the script is
ROOT_DIRECTORY = '.'  

# WHERE TO KEEP THE HASHES OF FILES
# !! keep .pkl extension !!
SCAN_STORAGE = 'hashes.pkl'

# LOGGING
LOG_FILE = 'app.log'
ALERT_FILE = 'alert.log'

# DON'T SCAN THESE AS THEY CHANGE EACH TIME
IGNORE_LIST = [SCAN_STORAGE, LOG_FILE, ALERT_FILE]

# HOW MANY SECONDS TO WAIT AFTER EACH SCAN
# you might want to have this one if you don't have much resources
SLEEP_TIME_SECONDS = 5
"""
SETTINGS END
"""
                        
#==============================================================================
# DRIVER FUNCTION
#==============================================================================
def driver():                       
    
    # start the initial scan
    file_handler.applog(LOG_FILE, "Starting the initial scan...")

    INITIAL_FILE_HASHES = scan()
   
    # save the initial scan dictionary of hashes
    file_handler.save_dict(INITIAL_FILE_HASHES, \
                           SCAN_STORAGE,\
                           LOG_FILE)
    file_handler.applog(LOG_FILE, "Initial scan completed!")
    
    
    
    # start the integrity check
    file_handler.applog(LOG_FILE, "Starting the integrity check...")
   
    while True:
        
        # get the file hashes
        new_hash = scan()
        
        # load the old hash
        old_hash = file_handler.load_dict(SCAN_STORAGE, \
                                          LOG_FILE)
        
        # compare two dict of hashes
        for diff in list(dictdiffer.diff(old_hash, new_hash)):         
            # ALERT
            if(diff[0]=="change"):
                msg = str(diff[0]) +',' + str( diff[1][0]) # + virusTotal.check_hash(diff)
                msg = msg + ',' + suspicionDetection.check(diff[2][0][0],diff[2][1])
            else:
                msg = str(diff[0]) +',' + str( diff[2][0][0])
                if(diff[0]=="add"):
                    msg = msg + ',' + suspicionDetection.check(diff[2][0][0],diff[2][0][1])
                else:
                    msg = msg + ',' + " - "
            change=str(diff[0])
            file_handler.alertlog(ALERT_FILE, msg,change,ROOT_DIRECTORY)
        
        # save the new hash
        file_handler.save_dict(new_hash, \
                               SCAN_STORAGE,
                               LOG_FILE)
        
        # wait
        time.sleep(SLEEP_TIME_SECONDS)
        


#==============================================================================
# SCAN
# Scan the directory tree and take hash of the files
# @return dictionary of hashes and file paths
#==============================================================================
def scan():
    
    # get dictonary of directories and files they contain
    directories = file_handler.search_directory_tree(ROOT_DIRECTORY, \
                                                     IGNORE_LIST, \
                                                     LOG_FILE)        
    
    # take hash
    file_hashes = dict()
    for path, files in directories.items():
        
        # look at each file at path
        for file in files:
            
            # get the full path name to the file
            file_dir = str(path) + "/" + str(file)
            
            # store the hash of the file
            file_hashes[file_dir] = hash_handler.hash_file_sha256(file_dir, \
                       LOG_FILE)
            
            
    # return dictionary with files path and hashes
    return file_hashes



# execute
if __name__ == "__main__":
    
    # start the driver
    print("\n------FILE INTEGRITY MONITOR------\n")
    
    while True:
        print("\nPress ctrl+C to stop the scan")
        print("Menu:")
        print("1. Scan for changes in directory")
        print("2. Regex based filters")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
    
        if choice == "1":
            print("Enter Root Directory: ")
            ROOT_DIRECTORY = input()
            try:
                driver()
            except KeyboardInterrupt:
                file_handler.applog(LOG_FILE, "Ending the integrity check...") 
                file_handler.disptable()
                continue 
        elif choice=="2":
            email=input("Enter Email Address: ")
            rg = input("Enter the Regular Expression: ")
            regex.search_regex(rg,ALERT_FILE,email)
            # print("Enter the Regular Expression: ")
            # regex.search_regex(input(),ALERT_FILE) 
        elif choice=="3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

    
    