import random
list = []
goal = []
penissortedlist = []
penis = 0
a=10000
for i in range(1,a+1):
    list.append(i)
for k in range(1,a+1):
    goal.append(k)
random.shuffle(list)
while penissortedlist != goal:
    print(penissortedlist+list)
    if list[penis] == min(list):
        penissortedlist.append(list[penis])
        list.remove(list[penis])
        penis = 0
    else:
        penis+=1
print("list sorted trust")