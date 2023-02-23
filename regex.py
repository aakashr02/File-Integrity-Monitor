from prettytable import PrettyTable
import re
import mail
def search_regex(regex,file,email):
    resultfile = open("result.log",'w')
    add=0
    change=0
    remove = 0
    myTable = PrettyTable(["Status", "File Name","Flag", "Time"])
    open_file = open(file,'r')
    for f in open_file:
        match = re.search(regex,str(f))
        if(match):
            # print(f.split(','))
            myTable.add_row(f.split(','))
            resultfile.write(f)
            if(f[0:3]=="add"):
                add += 1
            elif(f[0:6]=="change"):
                change += 1
            else:
                remove += 1
    open_file.close()
    print("\n\n------Filtered Records------\n")
    print("Add : ",add,"\tChange : ",change,"\tRemove : ",remove,"\n")
    print(myTable)
    resultfile.close()
    mail.mailing(email)
    print("Email has been sent successfully!!!!!!!!!!!")
    