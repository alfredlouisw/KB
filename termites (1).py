import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

def distance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

class swarm:
    def __init__(self):
        self.x = np.random.rand()*100 - 50
        self.y = np.random.rand()*100 - 50
        self.spd = 2
        self.carry = 0
        self.carried = 0
        self.count = 0

num_chip = 10000*25/1000


termites = [0 for b in range (50)]
chip = [0 for b in range(num_chip)]
for i in range (len(termites)):
    termites[i] = swarm()
for i in range (len(chip)):
    chip[i] = swarm()


tmax = 1000
cj=0
for t in range(tmax):


    fig = plt.figure()
    plt.gca().set_xlim([-50,50])
    plt.gca().set_ylim([-50,50])
    for i in range(len(termites)):
        if(termites[i].carry):
            plt.plot(termites[i].x, termites[i].y, 'bd')
        else:
            plt.plot(termites[i].x, termites[i].y, 'go')



    for i in range(len(chip)):
        if(chip[i].carried == 0):
            plt.plot(chip[i].x, chip[i].y, 'rs')

    for i in range(len(termites)):
        d = distance(termites[i].x,chip[0].x,termites[i].y,chip[0].y)
        if(termites[i].carry == 0):
            for j in range(len(chip)):

                if(d > distance(termites[i].x,chip[j].x,termites[i].y,chip[j].y)):
                    d = distance(termites[i].x,chip[j].x,termites[i].y,chip[j].y)
                    cj = j



            d = distance(termites[i].x,chip[cj].x,termites[i].y,chip[cj].y)
            rot = np.math.atan2(chip[cj].y - termites[i].y,chip[cj].x - termites[i].x)
            termites[i].x += termites[i].spd*np.math.cos(rot)
            termites[i].y += termites[i].spd*np.math.sin(rot)
            if(termites[i].x >= 50):
                termites[i].x = -50
            elif(termites[i].x <= -50):
                termites[i].x = 50
            elif(termites[i].y >=50):
                termites[i].y = 50
            elif(termites[i].y <=-50):
                termites[i].y = -50

            if(d < 1):
                chip[cj].x = termites[i].x
                chip[cj].y = termites[i].y
                termites[i].carry = 1
                chip[cj].carried = 1
        else:
            for j in range(len(chip)):

                if(d > distance(termites[i].x,chip[j].x,termites[i].y,chip[j].y) and j!=cj):
                    d = distance(termites[i].x,chip[j].x,termites[i].y,chip[j].y)
                    cj2 = j



            d = distance(termites[i].x,chip[cj2].x,termites[i].y,chip[cj2].y)
            rot = np.math.atan2(chip[cj2].y - termites[i].y,chip[cj2].x - termites[i].x)
            termites[i].x += termites[i].spd*np.math.cos(rot)
            termites[i].y += termites[i].spd*np.math.sin(rot)

            if(termites[i].x >= 50):
                termites[i].x = -50
            elif(termites[i].x <= -50):
                termites[i].x = 50
            elif(termites[i].y >=50):
                termites[i].y = 50
            elif(termites[i].y <=-50):
                termites[i].y = -50

            if(d < 1):
                chip[cj].x = chip[cj2].x+np.random.rand()*2-1
                chip[cj].y = chip[cj2].y+np.random.rand()*2-1
                termites[i].carry = 0
                chip[cj].carried = 0








    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)