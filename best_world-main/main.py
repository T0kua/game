import random
import time
import os
import pygame
from __init__ import *
x = random.randint(0,39)
y = random.randint(0,24)
#       0 1 2 3 4 5 6     7    8
obj = [[0,0,1,0,1,1,1,[y,x],10]]
"""
0 - тип растение - 0 ; животное - 1
1 - получение энергии с трупов 
2 - получение энергии солнца
3 - передвижение 
4 - срок жизни (1 - высокий / 0 - низкий)
5 - тип размножения 1 бесполое(растения)/0 половое (животные)
6 - жив 
7 - положение на карте X Y
8 - голод
"""
div = (__file__[0:-7]) #путь к папке файлом

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
day = 0
obj_max = 0 #наибольшее количество обьектов в симуляции было...
pos = []
for j in range(height // 10): # Y
	pos.append([])
	for i in range(width // 10): # X
		pos[j].append("^")

def flip() :
 pygame.display.flip()
try:
	file = open(f"{div}statistick.txt","r")
except:
	file = open(f"{div}statistick.txt","w")
file.close()
while len(obj) > 0 :
	if day+1 == 100 :
		try :
			file = open(f"{div}gen.txt","r")
			s = file.read()
			file.close()
			file = open(f"{div}gen.txt","w")
			file.write(s)
			file.write(f"======================\n")
			for i in range(len(obj)):
				file.write(f"{obj[i]}")
				file.write("\n")
			file.close()
		except :
			file = open(f"{div}gen.txt","w")
			file.write("""
0 - тип растение - 0 ; животное - 1
1 - получение энергии с трупов 
2 - получение энергии солнца
3 - передвижение 
4 - срок жизни (1 - высокий / 0 - низкий)
5 - тип размножения 1 бесполое(растения)/0 половое (животные)
6 - жив 
7 - положение на карте X Y
8 - голод
""")		
			file.write("=0 1  2  3  4  5  6     7      8=\n")
			for i in range(len(obj)):
				file.write(f"{obj[i]}")
				file.write("\n")
			file.close()
	if len(obj) > obj_max :
		obj_max = len(obj)
	file = open(f"{div}statistick.txt","r")
	state = file.read()
	file.close()
	file = open(f"{div}statistick.txt","w")
	file.write(state)
	day += 1
	file.write(f"   {day}|")
	#if len(obj) <= 50 :
	#print(obj)
	for k in pos :
		print(k)
	file.write(f"object {len(obj)}")
	print(f"{day}|object {len(obj)}")
	#time.sleep(0.5)
	clock.tick(fps)
	screen.fill(white)
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			obj = []
			file.write("\n%=    simulation abort       =%")
			continue
	for i in obj :
		if i[0] == 0 :
			pygame.draw.circle(screen,green,(i[7][1] * 10,i[7][0] * 10),5,0)
		if i[0] == 1 :
			pygame.draw.circle(screen,red,(i[7][1] * 10,i[7][0] * 10),5,0)
			#pygame.draw.rect(screen,red, (i[7][1] * 10,i[7][0] * 10,10,10),0)

	for i in range(height // 10):
		for k in range(width // 10) :
			if pos[i][k] == "%" :
				pygame.draw.circle(screen,black,(k * 10,i * 10),5,1)
				#pygame.draw.rect(screen ,black ,(k*10 ,i*10 ,10 ,10),0)
	flip()

	for i in obj :
		if i[6] == 0 : #для трупов
			pos[i[7][0]][i[7][1]] = "%"# отрисовка карты
			obj.remove([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
			continue
		else : #рисуем цифру
			pos[i[7][0]][i[7][1]] = str(i[0])# отрисовка карты

		if i[8] > 0 : #голод
			try :
				if i[1] == 1 : #если может получать энергию с трупов
					if pos[i[7][0] - 1][i[7][1] - 1] == "%" : #left-top
						i[8] -= random.randint(1,2)
						pos[i[7][0] - 1][i[7][1] - 1] = "^"
					elif pos[i[7][0] - 1][i[7][1]] == "%" :#top
						i[8] -= random.randint(1,2) 
						pos[i[7][0] - 1][i[7][1]] = "^" 
					elif pos[i[7][0] - 1][i[7][1] + 1] == "%" :#right
						i[8] -= random.randint(1,2)
						pos[i[7][0] - 1][i[7][1] + 1] = "^"
					elif pos[i[7][0]][i[7][0] - 1] == "%" :#left
						i[8] -= random.randint(1,2) 
						pos[i[7][0]][i[7][0] - 1] = "^" 
					elif pos[i[7][0]][i[7][0] + 1] == "%" :#right
						i[8] -= random.randint(1,2)
						pos[i[7][0]][i[7][0] + 1] = "^"
					elif pos[i[7][0] + 1][i[7][1] - 1] == "%" : #left-bottom
						i[8] -= random.randint(1,2)
						pos[i[7][0] + 1][i[7][1] - 1] = "^"
					elif pos[i[7][0] + 1][i[7][1]] == "%" :#top-bottom
						i[8] -= random.randint(1,2)  
						pos[i[7][0] + 1][i[7][1]] = "^"
					elif pos[i[7][0] + 1][i[7][1] + 1] == "%" :#right-bottom
						i[8] -= random.randint(1,2)
						pos[i[7][0] + 1][i[7][1] + 1] = "^"  
				elif i[2] == 1 :#если может получать энергию солнца 
					i[8] -= 1 #уменьшить голод
				else : #если голодает
					i[8] += 1 #увеличить голод
			except:
				print("#error$hunger")

		if i[8] <= 0 : #излишек энергии 
			if i[5] == 1 : # Y                                     #X
				x = [i[7][0] + random.choice([-1,0,1]) ,i[7][1] + random.choice([-1,0,1])]
				if(0<= x[1] < 40) and (0 <= x[0] < 25) :
					if pos[x[0]][x[1]] == "^":
						gen = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],x,10]
						if random.randint(0,gen_mutation_range) > gen_change : # мутации
							g = gen[random.choice([0,1,2,2,3,4,5,6])]
							if  gen[g] == 0 :
								gen[g] = 1
							elif gen[g] == 1 :
								gen[g] = 0
						if gen[6] == 1 :
							obj.append(gen)
				i[8] = hunger_last_bersday #действие требует энергии
		if day > dead_start :
			if i[4] == 1: #старость
				if random.randint(0,old1_range) > old1_dead :
					pos[i[7][0]][i[7][1]] = "%"
					obj.remove([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
					continue
			if i[4] == 0 : #старость
				if random.randint(0,old0_range) > old0_dead :
					pos[i[7][0]][i[7][1]] = "%"
					obj.remove([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
					continue

		if i[8] >= max_hunger : #голодная смерть
			pos[i[7][0]][i[7][1]] = "%"
			obj.remove([i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]])
			continue
		if i[3] == 1 :#перемещение
			x = [i[7][0] + random.choice([-1,0,1]),i[7][1] + random.choice([-1,0,1])]
			if(0<= x[1] < 40) and (0 <= x[0] < 25) :
				if pos[x[0]][x[1]] == "^" :
					i[7] = x
file.write("\n%=    simulation dead       =%")
file.write(f"\n============================================")
file.write("\n")
file.close()

try:
	file = open(f"{div}table.txt","r")
	state = file.read()
	file.close()
	file = open(f"{div}table.txt","w")
	file.write(state)
	file.write(f"\n{day}|{obj_max}")
	file.close()
except:
	file = open(f"{div}table.txt","w")
	file.write("day|max_object")
	file.write(f"\n{day}|{obj_max}")
	file.close()
