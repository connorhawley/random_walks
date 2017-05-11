import random
import statistics as stat
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def createlattice(width, height):
    lattice = np.zeros((width+3,height+3),dtype='int32')
    for row in lattice:
        row[0] = 1
        row[-1] = 1
    for i in range(width+3):
        lattice[0][i] = 1
        lattice[-1][i] = 1
    return lattice


def plot(pointsvisited, width, height):
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
    plt.title('Self-Avoiding Random Walk')
    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.plot(0, 0, '.b-')
    plt.text(0, 0, u'Start')
    graph, = plt.plot([], [], '.r-')

    def animate(i):
        graph.set_data(px[:i+1], py[:i+1])
        return graph

    animation = FuncAnimation(figure, animate, frames=len(px)+10, interval=75, repeat=False)
    plt.plot(0, 0, '.b-')
    plt.text(0, 0, u'Start')
    plt.show()


def walk(width, height, plotdata=False):
    x = width // 2
    y = height // 2
    pathlength = 0
    lattice = createlattice(width, height)
    lattice[x][y] = 1
    pointsvisited=[[x,y]]
    #0 North, 1 East, 2 South, 3 West
    while(0 < x < width+1
          and 0 < y < height+1):
        direction = random.randint(0, 3)
        if lattice[x][y + 1] == 1 and lattice[x][y - 1] == 1 and lattice[x - 1][y] == 1 and lattice[x + 1][y] == 1:
            break
        else:
            if direction == 0:                  #north y+1
                if lattice[x][y+1] != 1:        #if point not visited
                    y+=1
                    lattice[x][y] = 1          #mark as visited
                    pathlength += 1
                else:
                    continue
            elif direction == 1:                #east x+1
                if lattice[x+1][y] != 1:
                    x+=1
                    lattice[x][y] = 1
                    pathlength += 1
                else:
                    continue
            elif direction == 2:                #south y-1
                if lattice[x][y-1] != 1:
                    y-=1
                    lattice[x][y] = 1
                    pathlength += 1
                else:
                    continue
            elif direction == 3:                 #west x-1
                if lattice[x-1][y] != 1:
                    x-=1
                    lattice[x][y] = 1
                    pathlength += 1
                else:
                    continue
            pointsvisited.append([x, y])

    if plotdata:
        plot(pointsvisited, width, height) #plots the path
    return pathlength


def main():
    values = [walk(100,100, True)]
    print('Path length for 1 simulation: '+str(values[0]))

    values1 = [walk(100,100) for i in range(100)]
    averageLength = stat.mean(values1)
    standardDeviation = stat.stdev(values1)
    print('\nAverage Path length 100x100: ' + str(averageLength)+'\n'+'Standard Deviaton of Path Length 100x100: ' + str(standardDeviation))

    values2 = [walk(1000,1000) for i in range(100)]
    averageLength2 = stat.mean(values2)
    standardDeviation2 = stat.stdev(values2)
    print('\nAverage Path length 1000x1000: ' + str(averageLength2)+'\n'+'Standard Deviaton of Path Length 1000x1000: ' + str(standardDeviation2))

    input('\nPress enter to close.')
if __name__ == "__main__":
	main()