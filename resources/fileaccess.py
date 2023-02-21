from ctypes.wintypes import HANDLE
from hashlib import new
import win32file
import win32con
import os

def monitor_file_access(path):
    h_directory = win32file.CreateFile(
        path,
        win32con.GENERIC_READ,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )

    while True:
        results = win32file.ReadDirectoryChangesW(
            h_directory,
            2048,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            #win32con.FILE_NOTIFY_CHANGE_SIZE |
            #win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None
        )
        print(len(results))
        for action, file_name in results:
            print(action," : ",file_name,"\n")
            if action == 3:#win32con.FILE_ATTRIBUTE_READONLY:
               #dir_list = os.listdir(path)
               #for file in dir_list
               file_attributes = win32file.GetFileAttributes(path+"/"+file_name)
               #print(file_attributes)
               if (file_attributes==32):
                   print("File is writeable:", file_name)
               elif (file_attributes==33):
                   print("File is read only:", file_name)
               elif (file_attributes==34):
                   print("File is Hidden:", file_name)
               else:
                   print("File is Hidden and Readonly")
               print("\n")


try:
    monitor_file_access("D:\SEMESTER - 6\Cyber Security Project\File Integrity Monitor\sample")
except KeyboardInterrupt:
    print("Ended\n")

#attr = win32file.GetFileAttributes("sample.txt")
#print("attr : ",win32con.)