import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    
recovery_time = 4 # recovery time in time-steps
virality = 0.5    # probability that a neighbor cell is infected in 
                  # each time step                                                  

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = "S" # can be "S" (susceptible), "R" (resistant = dead), or 
                         # "I" (infected)
        self.time_infected = -1
        
    def infect(self):
        self.state = "I"
        self.time_infected = 0
    
    def process(self, adjacent_cells):
        
        if self.state == "I":
            self.time_infected += 1
            if random.random() < pdeath(self.time_infected,5,1):
                self.state = "R"
                return
            elif self.time_infected == recovery_time:
                self.state = "S"
                self.time_infected = 0
                return
            else:
                for single_adj in adjacent_cells:
                    if single_adj.state == "S":
                        if random.random() <= virality:
                            single_adj.infect()
            
        
class Map(object):
    
    def __init__(self):
        self.height = 150
        self.width = 150           
        self.cells = {}

    def add_cell(self, cell):
        coord = (cell.x, cell.y)
        
        self.cells[coord] = cell
    
    def display(self):
        image = []
        for row in range(self.width):
            row_cells = []
            for column in range(self.height):
                somecell = (row,column)
                if (somecell in self.cells):
                    if self.cells[somecell].state == "S":
                        row_cells.append((0.0,1.0,0.0))
                    elif self.cells[somecell].state == "R":
                        row_cells.append((0.5,0.5,0.5))
                    elif self.cells[somecell].state == "I":
                        row_cells.append((1.0,0.0,0.0))
                else:
                    row_cells.append((0.0,0.0,0.0))
            image.append(row_cells)
        
        plt.imshow(image)
    
    def adjacent_cells(self,x,y):
        coordinates = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
        adjacent = []
        for coordinate in coordinates:
            if coordinate in self.cells:
                adjacent.append(self.cells[coordinate])
        return adjacent
       
    def time_step(self):
        for coord in self.cells:
           self.cells[coord].process(self.adjacent_cells(coord[0],coord[1]))
        self.display()

            
def read_map(filename):
    
    m = Map()
    f = open(filename, 'r')
    
    for cell in f:
        cell_x = int(cell.strip("\n").split(",")[0])
        cell_y = int(cell.strip("\n").split(",")[1])
        c = Cell(cell_x,cell_y)
        
        m.add_cell(c)
    
    return m
