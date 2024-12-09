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
    
    
    

parteUno()
