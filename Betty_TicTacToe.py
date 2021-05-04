# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:26:02 2021

@author: beatriz garcia 
"""
import random

tablero = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]

conteo = 0
for i in range(3):
    for j in range(3):
        if (tablero[i][j]=="_"):
            conteo = conteo + 1
            

if (conteo == 9):
    inicio = []
    for i in range(3):
        for j in range(3):
            inicio.append((i,j))
    inicial = random.choice(inicio)
    tablero[inicial[0]][inicial[1]] = 'O'

for k in range(conteo):
    def recompensas(tablero):
        
    	# Evaluar por filas las victorias de X y O
    	for i in range(3) :	
    		if (tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]) :	
    			if (tablero[i][0] == 'X') :
    				return 1
    			elif (tablero[i][0] == 'O') :
    				return -1
    
    	# Evaluar por columnas las victorias de X y O
    	for j in range(3) :
    	
    		if (tablero[0][j] == tablero[1][j] and tablero[1][j] == tablero[2][j]) :
    		
    			if (tablero[0][j] == 'X') :
    				return 1
    			elif (tablero[0][j] == 'O') :
    				return -1
    
    	# Evaluar por diagonales las victorias de X y O
    	if (tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]) :
    	
    		if (tablero[0][0] == 'X') :
    			return 1
    		elif (tablero[0][0] == 'O') :
    			return -1
    
    	if (tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]) :
    	
    		if (tablero[0][2] == 'X') :
    			return 1
    		elif (tablero[0][2] == 'O') :
    			return -1
    
    	# Si nadie gana
    	return 0
    

        
    def betty(tablero, depth, isMax) :
    	score = recompensas(tablero)
        
    	if (score == 1) :
    		return score
    
    	if (score == -1) :
    		return score
        
    	if (score == 0 and isMovesLeft(tablero) == False) :
    		return 0
            
    	if (score == 0 and isMovesLeft(tablero) == True) :
    		if (isMax):
    			bestlist1 = []
    			for i in range(3) :		
    				for j in range(3) :
      
    					if (tablero[i][j]=='_') :
    				
    						tablero[i][j] = 'X'
      
    						# Recursividad
    						bestlist1.append( betty(tablero, depth + 1, not isMax) )
    						sumar = 0
    						value = 0
    						for t in range(len(bestlist1)):
    							sumar = sumar + bestlist1[t]
    						value = sumar / len(bestlist1)
  
    						tablero[i][j] = '_'
    			return value

    		else :
    			bestlist2 = []
    
    			for i in range(3) :		
    				for j in range(3) :
    			
    					if (tablero[i][j] == '_') :
    				
    						tablero[i][j] = 'O'
                        
    						# Recursividad
    						bestlist2.append(betty(tablero, depth + 1, not isMax) )

    						sumar = 0
    						value = 0
    						for t in range(len(bestlist2)):
    							sumar = sumar + bestlist2[t]
    						value = sumar / len(bestlist2)

    						tablero[i][j] = '_'
    			return value
    	return score 

        
    def isMovesLeft(tablero) :
    
    	for i in range(3) :
    		for j in range(3) :
    			if (tablero[i][j] == '_') :
    				return True
    	return False
        
    
    def findBestMove(tablero, par):
    	if k in par:
    		bestVal = -1000
    	if k not in par:
    		bestVal = 1000
    	bestMove = (-1, -1)
    
    	# Minimax 
    	for i in range(3) :	
    		for j in range(3) :
    			if (tablero[i][j] == '_') :
    				score = 0
    				# Verifica si hay lugares en donde puede ganar el oponente
    				if k in par:
    					tablero[i][j] = 'X'
    					score = recompensas(tablero)
    					if (score == 1):
    						tablero[i][j] = '_'
    						bestMove = (i, j, score)
    						return bestMove
    					tablero[i][j] = 'O'
    					score = recompensas(tablero)
    					if (score == -1):
    						tablero[i][j] = '_'
    						bestMove = (i, j, score)
    						return bestMove
    				else:
    					tablero[i][j] = 'O'
    					score = recompensas(tablero)
    					if (score == -1):
    						tablero[i][j] = '_'
    						bestMove = (i, j, score)
    						return bestMove
    					tablero[i][j] = 'X'
    					score = recompensas(tablero)
    					if (score == 1):
    						tablero[i][j] = '_'
    						bestMove = (i, j, score)
    						return bestMove
    
    				if k in par:
    					tablero[i][j] = 'X'
    				else:
    					tablero[i][j] = 'O'
                        
    				moveVal = betty(tablero, 0, False)
    				tablero[i][j] = '_'
    				# Nuevo mejor que el anterior
    				if (k in par and moveVal >= bestVal) :			
    					bestMove = (i,j,moveVal)
    					bestVal = moveVal
    					if (len(options) > 0):
    						for y in range(len(options)):
    							if (moveVal > options[0][2]):
    								options.pop(0)
    					options.append(bestMove)
    				if (k not in par and moveVal <= bestVal) :			
    					bestMove = (i,j,moveVal)
    					bestVal = moveVal
    					if (len(options) > 0):
    						for t in range(len(options)):
    							if (moveVal < options[0][2]):
    								options.pop(0)
    					options.append(bestMove)
    	

    	if len(options) == 0:
    		return 'termina'
    	else:
    		return random.choice(options)

    options = []
    par = [0,2,4,6,8]
            
    bestMove = findBestMove(tablero, par)                    
    if bestMove !='termina':
        print()
        if k in par:
            print("El movimiento óptimo para 'X' es:","Fila", bestMove[0], " Columna", bestMove[1])
        else:
            print("El movimiento óptimo para 'O' es:","Fila", bestMove[0], " Columna", bestMove[1])
        
        if k in par:
            tablero[bestMove[0]][bestMove[1]] = 'X'
        else:
            tablero[bestMove[0]][bestMove[1]] = 'O' 
        print("Tablero con el movimiento óptimo:")
        for i in range(3):
            print (tablero[i][0]+str('|'), tablero[i][1]+str('|'), tablero [i][2])
        if (recompensas(tablero) == 1 or recompensas(tablero)==-1):
            break
