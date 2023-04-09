import pefile
import subprocess
#1.Import table analysis: 
#Counting no of times it counted as suspicious or not  by different ways
suspicious=0
nsuspicious=0
#Checking whether no of imports is greater 100
def check_imports(filename):
    pe = pefile.PE(filename)
    num_imports = len(pe.DIRECTORY_ENTRY_IMPORT)
    if num_imports > 100:
        return True
    else:
        return False
#2.Section name analysis
def print_section_names(filename):
    pe = pefile.PE(filename)
    validnames=['.text','.data','.bss','.rdata','.edata','.idata','.reloc','.tls','.rsrc']
    l=0;
    for section in pe.sections:
        if section.Name.decode() not in validnames:
            return True
    return False
#3. Entry point analysis
def check_entry_point(filename):
    pe = pefile.PE(filename)
    entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    if entry_point < pe.sections[0].VirtualAddress or entry_point >= pe.sections[-1].VirtualAddress + pe.sections[-1].Misc_VirtualSize:
        return True
    else:
         return False
#4.Code section analysis
def check_code_section_size(filename):
    pe = pefile.PE(filename)
    code_section = pe.sections[0]
    code_size = code_section.SizeOfRawData
    if code_size < 1000:
         return True
    elif code_size > 100000:
         return True
    else:
        return False
#5 String analysis

def check_strings(filename):
    pe = pefile.PE(filename)
    for section in pe.sections:
        section_data = section.get_data()
        try:
            decoded_strings = section_data.decode()
        except UnicodeDecodeError:
            continue

        suspicious_strings = [
            "CreateRemoteThread"
,"LoadLibraryA"
,"GetProcAddress"
,"VirtualAlloc"
,"WriteProcessMemory"
,"Shellcode"
,"CreateProcessA"
,"TerminateProcess"
,"WinExec"
,"ExitProcess"
,"ExitThread"
,"SetWindowsHookExA"
,"RegOpenKeyExA"
,"RegQueryValueExA"
,"RegSetValueExA"
,"RegCreateKeyExA"
,"InternetConnectA"
,"InternetOpenUrlA"
,"HttpSendRequestA"
,"InternetReadFile"
        ]
        k=0
        for suspicious_string in suspicious_strings:
            if suspicious_string in decoded_strings:
                return True
    return False


#6.relocation table

def check_packing1(filename):
    pe = pefile.PE(filename)

    # Check if the file has any imports
    r=0
    if not hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        return True

    # Check if the file has a relocations table
    if not hasattr(pe, "DIRECTORY_ENTRY_BASERELOC"):
       return True
    if r==0:
        return False

def check_packing(filename):# Run PEiD on the file    
    peid_output = subprocess.run(["PEiD.exe", filename], capture_output=True, text=True)
    
    # Check if the output indicates the file is packed    
    if "Packer detected" in peid_output.stdout:
        return True
    else:
        return False

# if __name__ == "__main__":
def check_exe(filename):
    c=False
    #c=c|print_section_names(filename)
    c=c|check_imports(filename)
    c=c|check_entry_point(filename)
    #c=c|check_code_section_size(filename)
    c=c|check_strings(filename)
    c=c|check_packing(filename)
    if c==True:
        # print("File is detected as Suspicious")
        return 1
    else:
        # print("File is detected not as Suspicious")
        return 0



                
