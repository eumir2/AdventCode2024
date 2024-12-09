
#
#
#PARTE UNO
#
#

def parte1():
    f = open("input.txt")
    
    
    reports = []
    
    for i in f:
        line = i.split()
        reports.append(list(map(int, line)))
        
    #print(reports)
    safe_reports = 0;
    for r in reports:
        if(checkReportPartOne(r)):
            safe_reports += 1
    
    print(safe_reports)    
  
def checkReportPartOne(report):
    cresc = True
    if(report[0] > report[1]):
        cresc = False
    
    for r in range(len(report)-1):
        if cresc:
            if report[r] > report[r+1] or abs(report[r] - report[r+1]) > 3 or abs(report[r] - report[r+1]) < 1:
                #print(report," false")
                return False
        else:
            if report[r] < report[r+1] or abs(report[r] - report[r+1]) > 3 or abs(report[r] - report[r+1]) < 1:
                #print(report," false")
                return False
    #print(report," true")
    return True; 

#
#
#PARTE DUE
#
#
def parte2():
    f = open("input.txt")
    
    
    reports = []
    
    for i in f:
        line = i.split()
        reports.append(list(map(int, line)))
        
    #print(reports)
    safe_reports = 0;
    for r in reports:
        tmp = checkReportPartTwo(r)
        #print(r,tmp)
        if(tmp):
            safe_reports += 1
    
    print(safe_reports)
  
#controllo che per quelli unsafe togliendo un elemento sia safe    
def checkReportPartTwo(report):
    if checkReportPartOne(report) == False:
        for i in range(len(report)):
            if checkReportPartOne(report[:i]+report[i+1:]):
                return True
    else:
        return True

def defineOrder(report):
    while len(report) > 1:
        if report[0] == report[1]:
            del report[0]
        elif report[0] > report[1]:
            return False
        else:
            return True
        
parte2()
