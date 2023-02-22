from prettytable import PrettyTable
import re
def search_regex(regex,file):
    add=0
    change=0
    remove = 0
    myTable = PrettyTable(["Status", "File Name","Flag", "Time"])
    myTable
    open_file = open(file,'r')
    for f in open_file:
        match = re.search(regex,str(f))
        if(match):
            myTable.add_row(f.split(','))
            if(f[0:3]=="add"):
                add += 1
            elif(f[0:6]=="change"):
                change += 1
            else:
                remove += 1
    print("\n\n------Filtered Records------\n")
    print("Add : ",add,"\tChange : ",change,"\tRemove : ",remove,"\n")
    print(myTable)
