import pprint 

#
#
#PARTE UNO
#
#
import re
def parteUno():
    f = open("input.txt")
    s = ""
    for line in f:
        s += line
    
    
    #trovo tutte le mul valide
    valid = re.findall("mul\(\d+,\d+\)",s)
    #print(valid)
    
    product = 0;
    for v in valid:
        #string formatting
        v = re.sub("mul\(","",v)
        v = re.sub("\)","",v)
        values = list(map(int,v.split(",")))
        product += values[0] * values[1]
        
        
    print(product)
    
def parteDue():
    f = open("input.txt")
    s = ""
    
    do  = "do()"
    dont = "don't\(\)"
    for line in f:
        s += line
        
    prettyS = "".join(s.split())
    #splitto prima per dont
    split1= re.split(dont,prettyS)
    
    #trovo il primo do che abilita e tolgo l'inizio
    todo = []
    #aggiungo la prima che è sempre da controllare
    todo.append(split1[0])
    for s in range(1,len(split1)):
        index = split1[s].find(do)
        #sottostringa che elimina la parte iniziale da non eseguire
        if index != -1:
            todo.append(split1[s][index:])
    
    sum_of_prod = 0
    #ciclo lungo le stringhe e calcolo
    for t in todo:
        #trovo tutte le mul valide
        valid = re.findall("mul\(\d+,\d+\)",t)
        
        for v in valid:
            #string formatting
            v = re.sub("mul\(","",v)
            v = re.sub("\)","",v)
            values = list(map(int,v.split(",")))
            sum_of_prod += values[0] * values[1]
            
    print(sum_of_prod)    
    
    
    
    

parteDue()
