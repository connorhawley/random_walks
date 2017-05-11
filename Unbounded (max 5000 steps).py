import random, math
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def createlattice(width, height):
    lattice = np.zeros((width+3,height+3),dtype='int32')
    return lattice


def plot(pointsvisited, width, height): #plot the walked path
    for coordinate in pointsvisited:
        coordinate[0] -= width//2
        coordinate[1] -= height//2
    px = []
    py = []
    for coordinate in pointsvisited:
        px.append(coordinate[0])
        py.append(coordinate[1])
    figure = plt.figure()
    plt.xlim(min(px)-5, max(px)+5)
    plt.ylim(min(py)-5,max(py)+5)
    plt.title('Self-Avoiding Random Walk, No Lattice Boundary')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.plot(0,0,'.b-')
    plt.text(0,0,u'Start')

    graph, = plt.plot([], [], '.r-')

    def animate(i):
        graph.set_data(px[:i+1], py[:i+1])
        return graph

    animation = FuncAnimation(figure, animate, frames=len(px)+10, interval=75, repeat=False)

    plt.plot(0,0,'.b-')
    plt.text(0,0,u'Start')
    plt.show()


def walk(width, height, plotdata=False):
    #start_time = time.clock()
    x = width//2
    y = height//2
    numsteps = 0
    lattice = createlattice(width, height)
    lattice[x][y] = 1
    pointsvisited=[[x,y]]
    #0 North, 1 East, 2 South, 3 West
    while(numsteps < 5000):
        direction = random.randint(0, 3)
        if (lattice[x][y + 1] == 1 and lattice[x][y - 1] == 1 and lattice[x - 1][y] == 1 and lattice[x + 1][y] == 1):
            #print('stuck at point ' + str((x-width//2,y-height//2)))
            break
        else:
            if direction == 0:                  #north y+1
                if lattice[x][y+1] != 1:        #check if point is visited
                    y+=1
                    lattice[x][y] = 1           #mark as visited if it has not been
                    numsteps += 1
                else:
                    continue
            elif direction == 1:                #east x+1
                if lattice[x+1][y] != 1:
                    x+=1
                    lattice[x][y] = 1
                    numsteps += 1
                else:
                    continue
            elif direction == 2:                #south y-1
                if lattice[x][y-1] != 1:
                    y-=1
                    lattice[x][y] = 1
                    numsteps += 1
                else:
                    continue
            elif direction == 3:                 #west x-1
                if lattice[x-1][y] != 1:
                    x-=1
                    lattice[x][y] = 1
                    numsteps += 1
                else:
                    continue
            pointsvisited.append([x,y])



    distance = math.hypot(width//2 - pointsvisited[-1][0], height//2 - pointsvisited[-1][1]) #distance between start and end points
    latticesize = (max(coord[0] for coord in pointsvisited) - min(coord[0] for coord in pointsvisited)) * \
                  ((max(coord[1] for coord in pointsvisited)) - min(coord[1] for coord in pointsvisited))

    if plotdata:
        plot(pointsvisited, width, height) #plot the walk

    return [numsteps, distance, latticesize]


def main():
    values = [walk(10000,10000, True)]
    distance = values[0][1]
    latticesize = values[0][2]

    print('--1 simulation--\nDistance: '+str(distance)+
                     '\n'+'Lattice Size: '+str(latticesize))


    values1 = [walk(10000,10000) for i in range(10)]
    distlist = [_[1] for _ in values1]
    distavg = stat.mean(distlist)
    distmedian = stat.median(distlist)
    distvar = stat.variance(distlist, distavg)
    diststdev = stat.stdev(distlist, distavg)

    latticelist = [_[2] for _ in values1]
    latticeavg = stat.mean(latticelist)
    latticemedian = stat.median(latticelist)
    latticevar = stat.variance(latticelist, latticeavg)
    latticestdev = stat.stdev(latticelist, latticeavg)
    print('\n--10 simulations--\n'
            'Average Distance: ' + str(distavg) +
            '\nMedian Distance: '+ str(distmedian) +
            '\nVariance of Distance: ' + str(distvar) +
            '\nStdev of Distance: '+ str(diststdev)     +
            '\nAverage Lattice Size: ' + str(latticeavg) +
            '\nMedian Lattice Size: ' + str(latticemedian) +
            '\nVariance of Lattice Size: ' + str(latticevar) +
            '\nStdev of Lattice Size: ' + str(latticestdev))

    values2 = [walk(10000,10000) for i in range(100)]
    distlist = [_[1] for _ in values2]
    distavg = stat.mean(distlist)
    distmedian = stat.median(distlist)
    distvar = stat.variance(distlist, distavg)
    diststdev = stat.stdev(distlist, distavg)

    latticelist = [_[2] for _ in values2]
    latticeavg = stat.mean(latticelist)
    latticemedian = stat.median(latticelist)
    latticevar = stat.variance(latticelist, latticeavg)
    latticestdev = stat.stdev(latticelist, latticeavg)


    print('\n--100 simulations--\n'
            'Average Distance: ' + str(distavg) +
            '\nMedian Distance: '+ str(distmedian) +
            '\nVariance of Distance: ' + str(distvar) +
            '\nStdev of Distance: '+ str(diststdev)     +
            '\nAverage Lattice Size: ' + str(latticeavg) +
            '\nMedian Lattice Size: ' + str(latticemedian) +
            '\nVariance of Lattice Size: ' + str(latticevar) +
            '\nStdev of Lattice Size: ' + str(latticestdev))

    values3 = [walk(10000,10000) for i in range(1000)]
    distlist = [_[1] for _ in values3]
    distavg = stat.mean(distlist)
    distmedian = stat.median(distlist)
    distvar = stat.variance(distlist, distavg)
    diststdev = stat.stdev(distlist, distavg)

    latticelist = [_[2] for _ in values3]
    latticeavg = stat.mean(latticelist)
    latticemedian = stat.median(latticelist)
    latticevar = stat.variance(latticelist, latticeavg)
    latticestdev = stat.stdev(latticelist, latticeavg)

    print(('\n--1000 simulations--\n'
            'Average Distance: ' + str(distavg) +
            '\nMedian Distance: '+ str(distmedian) +
            '\nVariance of Distance: ' + str(distvar) +
            '\nStdev of Distance: '+ str(diststdev)     +
            '\nAverage Lattice Size: ' + str(latticeavg) +
            '\nMedian Lattice Size: ' + str(latticemedian) +
            '\nVariance of Lattice Size: ' + str(latticevar) +
            '\nStdev of Lattice Size: ' + str(latticestdev)))

    input('\nPress enter to close.')
if __name__ == "__main__":
    main()