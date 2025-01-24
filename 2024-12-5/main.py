#
#
#PARTE UNO
#
#
# 

def parteUno():
    f = open("input.txt")
    
    flag = True
    
    page_ordering_rules = {}
    updates = []
    for line in f:
        if line == '\n':
            flag = False
        
        line = line.strip()
         
        if flag:
            f,s = line.split("|")
            if f in page_ordering_rules:
                page_ordering_rules[f].append(line)
            else:
                page_ordering_rules[f] = [line]
            if s in page_ordering_rules:
                page_ordering_rules[s].append(line)
            else:
                page_ordering_rules[s] = [line]
        else:
            updates.append(line.split(","))
            
    #rimuovo elemento vuoto 
    updates = updates[1:]
    
    #print(page_ordering_rules)
    
    correct_updates = []
    for single_update in updates:
        flag = True
        for u in single_update:
            for p in page_ordering_rules[u]:
                before, after = p.split("|") 
                if before in single_update and after in  single_update and single_update.index(before) > single_update.index(after):
                    flag = False
        if flag:
            correct_updates.append(single_update)
        
    sum_of_middle_element = 0
    for cu in correct_updates:
        middle_element = int(cu[len(cu)//2])
        sum_of_middle_element += middle_element
    
    print(sum_of_middle_element)
        
        
parteUno()