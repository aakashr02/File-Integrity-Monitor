from tabnanny import check
import pe_file
import virusTotal

# Function to detect Suspicion  
def check(filename,hash):
    
    #Initialize Suspicion Flag to 0
    flag = 0
    
    # if the file is exe analyze using pefile module
    if(filename[-1:-4]=="exe"):
        flag = flag | pe_file.check_exe(filename)
    
    # For all files get suspicion flag from virusTotal API
    vt_result = virusTotal.VT_Request(hash)
    if(vt_result == -1):
        return "Undetermined" 
    flag = flag | vt_result
    if(flag):
        return "Suspicious"
    else:
        return "Safe"