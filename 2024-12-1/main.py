
def parte1():
    f = open("input.txt")
    
    lista_uno = []
    lista_due = []
    
    for i in f:
        riga = i.split()
        #print(riga)
        lista_uno.append(int(riga[0]))
        lista_due.append(int(riga[1]))
            
    distanza = 0
    lista_uno.sort()
    lista_due.sort()
    
    for i in range(len(lista_uno)):
        distanza += abs(lista_uno[i] - lista_due[i])
        

def parte2():
    f = open("input.txt")
    
    list_one = []
    frequency = {}
    
    for i in f:
        riga = i.split()
        #print(riga)
        list_one.append(int(riga[0]))
        if int(riga[1]) in frequency:
            frequency[int(riga[1])] = frequency.get(int(riga[1])) + 1
        else:
            frequency[int(riga[1])] = 1
            
            
    similarity_score = 0
    for i in range(len(list_one)):
        if list_one[i] in frequency:
            similarity_score += list_one[i] * frequency.get(list_one[i])
    
    print(similarity_score)


#parte1()

parte2()