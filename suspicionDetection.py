from tabnanny import check
import pe_file
import virusTotal

# filename = "D:\SEMESTER - 6\Cyber Security Project\File-Integrity-Monitor-master\File-Integrity-Monitor-master\dist\driver.exe"
  
def check(filename,hash):
    flag = 0
    if(filename[-1:-4]=="exe"):
        flag = flag | pe_file.check_exe(filename)
    
    flag = flag | virusTotal.VT_Request(hash)
    if(flag):
        return "Suspicious"
    else:
        return "Safe"