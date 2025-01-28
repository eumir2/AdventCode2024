import re
import pprint
#
#
#PARTE UNO
#
#
def parteUno():
    file = open("input.txt")
    direzioni = "V><^"
    
    #griglia di memorizzazione
    grid = []
    
    #indici del punto di partenza + flag
    col = 0
    row = 0
    flag = True
    
    #leggo il fl
    for line in file:
        if any(char in line for char in f"[{direzioni}]"):
            match = re.search(f"[{direzioni}]", line)
            col = match.start()
            flag = False
        grid.append(line)
        if flag:
            row += 1
    
    print(row,col)
    '''
    le direzioni sono
    V -> aumento riga
    ^ -> diminuisco riga
    < -> diminuisco colonna
    > -> aumento colonna 
    '''
    counter = 1
    dir = grid[row][col]
    nextRow = row
    nextCol = col
    while (nextRow >= 0 and nextRow < len(grid)) and (nextCol >= 0 and nextCol < len(grid[0])):
        
        if grid[nextRow][nextCol] == '#':
            #devo ruotare la direzione
            if dir == '^':
                nextRow += 1
                dir = '>'
            elif dir == '>':
                nextCol -= 1
                dir = 'V'
            elif dir == '<':
                nextCol += 1
                dir = '^'
            else:
                dir = '<'
                nextRow -= 1
        else:  
            if grid[nextRow][nextCol] == '.':
                counter += 1  
            tmp = list(grid[nextRow])
            tmp[nextCol] = dir
            grid[nextRow] = "".join(tmp)
            
            if dir == '^':
                nextRow -= 1
            elif dir == '>':
                nextCol += 1
            elif dir == '<':
                nextCol -= 1
            else:
                nextRow += 1
            
        
        
        

       
        
    
    print(counter)
    
    

    
    
    
    
    
    
    
    
    
parteUno()