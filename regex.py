from prettytable import PrettyTable
import re
import mail

# function to search log records for the given regex
def search_regex(regex,file,email):
    resultfile = open("result.log",'w')
    
    #Initializing variables to count the number of add/modify/delete satisfying the regex
    add=0
    change=0
    remove = 0
    myTable = PrettyTable(["Status", "File Name","Flag", "Time"])
    open_file = open(file,'r')
    
    #searching regex
    for f in open_file:
        match = re.search(regex,str(f))
        if(match):
            #adding records to prettyTable formatter 
            myTable.add_row(f.split(','))
            resultfile.write(f)
            if(f[0:3]=="add"):
                add += 1
            elif(f[0:6]=="change"):
                change += 1
            else:
                remove += 1
    open_file.close()
    
    # Displaying Results
    print("\n\n------Filtered Records------\n")
    print("Add : ",add,"\tChange : ",change,"\tRemove : ",remove,"\n")
    print(myTable)
    resultfile.close()
    
    #Mailing the Results
    try:
        mail.mailing(email)
        print("Email has been sent successfully!!!!!!!!!!!")
    except Exception as e:
        print("Could not send mail")
    