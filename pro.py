import gtable
import matplotlib.pylab as pl

names = ["Python","WT","DBMS","Flat","CO", "OS"]
Labs = ["Lab1", "Lab2","Lab3"]
subphrs = 5 #25
labhrs = 9
extrahrs = 8
examhrs = 6


def conv(table):
    global names, Labs
    for i in table:
        for j in range(len(i)):
            if i[j] == 'free' or i[j] == 'Test' or i[j] == 'Revision':
                continue
            if int(i[j]) < 7:
                if int(i[j]) == 0:
                    i[j] = 'Unallocated'
                else:
                    i[j] = names[int(i[j])-1]
            else:
                i[j] = Labs[int(i[j]) - 25 ]
    names = names[1:]
    names.append(names[0])
    Labs = Labs[1:]
    Labs.append(Labs[0])
    return table


def plot(table,x):
    ny = len(table)
    nx = len(table[0])
    pl.figure("Section "+ str(x+1))
    tb = pl.table(cellText=table, loc=(0,0), cellLoc='center')
    
    ax = pl.gca()
    ax.set_xticks([])
    ax.set_yticks([])

    pl.show()


table = gtable.gentable()
table[[5,2]] = table[[2,5]]
table = gtable.add_freep(table).tolist()

for i in range(4,8):
    table[1][i] , table[2][i] = 'Revision' , table[1][i]
table[2][3] = 'free'

table[2][0] = 'Test'
table[2][1] = 'Test'

table[4][6] = 'free'


x = 2
while x==2 or x==1 or table[x][6]=='free':
    x = gtable.ran(4)
table[x][6] , table[2][2] = 'free' , table[x][6]


x = 2
while x==2 or x == 1 or table[x][6]=='free':
    x = gtable.ran(4)

table[x][6] , table[2][3] = 'free' , table[x][6]


import copy

sec = []
for i in range(4):
    sec.append(copy.deepcopy(list(table[:])))
for i in range(4):
    conv(sec[i])
    plot(sec[i],i)
