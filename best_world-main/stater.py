import matplotlib.pyplot as plt
div = (__file__[0:-9]) #путь к папке файлом
file = open(f"{div}table.txt","r")
state = file.read()
file.close()
state = state.split("\n")
state.remove("day|max_object")

day = []
obj = []
for i in range(len(state)) :
	state[i] = state[i].split("|")
state.sort()
for i in range(len(state)):
	state[i][0],state[i][1] = state[i][1],state[i][0]
print(state)
for i in range(len(state)):
	day.append(state[i][0])
	obj.append(state[i][1])
plt.plot(day,obj)
plt.xlabel("max_object")
plt.ylabel("day")
plt.grid(True)
plt.show()