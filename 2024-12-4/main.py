import pprint
import numpy as np
#
#
#PARTE UNO
#
# 

def parteUno():
    f = open("input.txt")
    
    
    # Lettura da file
    with open("input.txt") as f:
        data = [list(line.strip()) for line in f]
        
    #print(data)
    matrix = np.array(data)  
    
    #counter per i valori
    counter = 0   
    #stringa base
    base = 'XMAS'
    
    # Definiamo i vettori direzionali
    direzioni = [
        (0, 1),   # Destra
        (0, -1),  # Sinistra
        (1, 0),   # Sotto
        (-1, 0),  # Sopra
        (1, 1),   # Diagonale basso-destra
        (1, -1),  # Diagonale basso-sinistra
        (-1, 1),  # Diagonale alto-destra
        (-1, -1)  # Diagonale alto-sinistra
    ]
     
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
           for dir in direzioni:
                if checkParola(matrix,i,j,dir, base):
                    counter += 1
                
    print(counter)                 
    
def checkParola(matrix, r,c,direzione, parola):
    n,m = matrix.shape
    
    delta_r, delta_c = direzione
    
    for k in range(len(parola)):
        nr = r + delta_r * k
        nc = c + delta_c * k
        
        #controllo limiti
        if nr >= n or nr < 0 or nc >= m or nc < 0:
            return False
        if matrix[nr,nc] != parola[k]:
            return False
        
    return True

def parteDue():
    f = open("input.txt")
    
    
    # Lettura da file
    with open("input.txt") as f:
        data = [list(line.strip()) for line in f]
        
    #print(data)
    matrix = np.array(data)
    
    counter = 0
    
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 'A':
                if checkCroce(matrix, i,j,):
                    counter += 1

    print(counter)
    
def checkCroce(matrix, r, c):
    n,m = matrix.shape
    d_m_dx = r - 1, c + 1
    d_m_sx = r + 1, c - 1
    
    d_M_dx = r + 1, c + 1
    d_M_sx = r -1, c - 1 
    
    if indici_validi(n, m, *d_m_dx) and indici_validi(n, m, *d_m_sx) and indici_validi(n, m, *d_M_dx) and indici_validi(n, m, *d_M_sx):
        tmp1 = matrix[d_M_sx[0],d_M_sx[1]]+matrix[r,c]+matrix[d_M_dx[0],d_M_dx[1]]
    
        tmp2 = matrix[d_m_sx[0],d_m_sx[1]]+matrix[r,c]+matrix[d_m_dx[0],d_m_dx[1]]

        if sorted(tmp1) == sorted(tmp2) == sorted("MAS"):
            return True
        else:
            return False
    
    return False
 
def indici_validi(n, m, r, c):
    return 0 <= r < n and 0 <= c < m   
    
    
#parteUno()

parteDue()