# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:26:02 2021

@author: tableroeatr
"""
import random

tablero = [
	[ '_', '_', '_' ],
	[ '_', 'O', '_' ],
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
    				#print(tablero[i][0], tablero[i][1], tablero[i][2],'entraf1',i)
    				return 1
    			elif (tablero[i][0] == 'O') :
    				#print('entraf2',i)
    				return -1
    
    	# Evaluar por columnas las victorias de X y O
    	for j in range(3) :
    	
    		if (tablero[0][j] == tablero[1][j] and tablero[1][j] == tablero[2][j]) :
    		
    			if (tablero[0][j] == 'X') :
    				#print('entrac1')
    				return 1
    			elif (tablero[0][j] == 'O') :
    				#print('entrac2')
    				return -1
    
    	# Evaluar por diagonales las victorias de X y O
    	if (tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]) :
    	
    		if (tablero[0][0] == 'X') :
    			#print('entrad1')
    			return 1
    		elif (tablero[0][0] == 'O') :
    			#print('entrad2')
    			return -1
    
    	if (tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]) :
    	
    		if (tablero[0][2] == 'X') :
    			#print('entrad3')
    			return 1
    		elif (tablero[0][2] == 'O') :
    			#print('entrad4')
    			return -1
    
    	# Si nadie gana
    	return 0
    

        
    def betty(tablero, depth, isMax) :
#    	print("tablero minimax")
#    	for r in range(3):
#    		print (tablero[r][0]+str('|'), tablero[r][1]+str('|'), tablero [r][2])

    	score = recompensas(tablero)
#    	print("score", score)
        
    	if (score == 1) :
#    		print("score 1")
    		return score
    
    	if (score == -1) :
#    		print("score -1")
    		return score
        
    	if (score == 0 and isMovesLeft(tablero) == False) :
    		return 0
            
    	if (score == 0 and isMovesLeft(tablero) == True) :
    		if (isMax):
#    			print("entra isMax")
    			bestlist1 = []
    			for i in range(3) :		
    				for j in range(3) :
      
    					if (tablero[i][j]=='_') :
    				
    						tablero[i][j] = 'X'
      
    						# Recursividad
    						bestlist1.append( betty(tablero,
    												depth + 1,
    												not isMax) )
#    						print(bestlist1)
#    						best = max(bestlist1)
    						sumar = 0
    						value = 0
    						for t in range(len(bestlist1)):
    							sumar = sumar + bestlist1[t]
    						value = sumar / len(bestlist1)
#    						print("best maximizador", best, "i, j =", i, j)
  
#    						print("tablero best maximizador")
#    						for r in range(3):
#    							print (tablero[r][0]+str('|'), tablero[r][1]+str('|'), tablero [r][2])

    						tablero[i][j] = '_'
#    			print("value1", value)
    			return value

    		else :
#    			print("entra not isMax")
    			bestlist2 = []
    
    			for i in range(3) :		
    				for j in range(3) :
    			
    					if (tablero[i][j] == '_') :
    				
    						# Make the move
    						tablero[i][j] = 'O'
                        
    						# Recursividad
    						bestlist2.append(betty(tablero,
    												depth + 1,
    												not isMax) )
#    						print(bestlist2)
#    						best = min(bestlist2)
    						sumar = 0
    						value = 0
    						for t in range(len(bestlist2)):
    							sumar = sumar + bestlist2[t]
    						value = sumar / len(bestlist2)
#    						print("best minimizador", best, "i, j =", i, j)

#    						print("tablero best minimizador")
#    						for r in range(3):
#    							print (tablero[r][0]+str('|'), tablero[r][1]+str('|'), tablero [r][2])

    						tablero[i][j] = '_'
#    			print("value2", value)
    			return value
#    	print("return score")
    	return score 

        
    def isMovesLeft(tablero) :
    
    	for i in range(3) :
    		for j in range(3) :
    			if (tablero[i][j] == '_') :
    				return True
    	return False
        
    
    ###### Agregar algo sobre la función de valor para calcular posibles 
    ###### jugadas futuras y en base a la probabilidad, calcularlo.
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
#    				print("moveval", moveVal, "i, j =", i, j)

#    				print("tablero findbestmove", moveVal)
#    				for r in range(3):
#    					print (tablero[r][0]+str('|'), tablero[r][1]+str('|'), tablero [r][2])
    				tablero[i][j] = '_'
    				# Nuevo mejor que el anterior
    				if (k in par and moveVal >= bestVal) :			
    					bestMove = (i,j,moveVal)
    					bestVal = moveVal
#    					print("bestmove", bestMove, "options", options, "len", len(options))
    					if (len(options) > 0):
    						for y in range(len(options)):
    							if (moveVal > options[0][2]):
    								options.pop(0)
    					options.append(bestMove)
    				if (k not in par and moveVal <= bestVal) :			
    					bestMove = (i,j,moveVal)
    					bestVal = moveVal
#    					print("bestmove", bestMove,"options", options, "len", len(options))
    					if (len(options) > 0):
    						for t in range(len(options)):
    							if (moveVal < options[0][2]):
    								options.pop(0)
    					options.append(bestMove)
    	

    	if len(options) == 0:
    		return 'termina'
    	else:
#    		print()
#    		print("opciones", options)
#    		print("El valor del mejor movimiento es :", bestVal)
    		return random.choice(options)
#    	return bestMove    

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
#        print("valor mejor mov",bestMove[2])
        if (recompensas(tablero) == 1 or recompensas(tablero)==-1):
            break