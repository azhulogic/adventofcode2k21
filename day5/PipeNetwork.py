# Alex Zhu
# 12/14/21
# Advent of Code - DAY FIVE
import re

class PipeNetwork:
    class Pipe:
        def __init__(self,str) -> None:
            nums = re.findall('\d+', str)

            self.x1 = int(nums[0])
            self.y1 = int(nums[1])
            self.x2 = int(nums[2])
            self.y2 = int(nums[3])
            
            return

        def __str__(self) -> str:
            return "{0},{1} -> {2},{3}".format(self.x1,self.y1,self.x2,self.y2)

        def __repr__(self) -> str:
            return str(self)

        def get_ends(self):
            """Getter, returns int tuple tuple: (x1,y1),(x2,y2)"""
            return ((self.x1,self.y1),(self.x2,self.y2))

        def points_between(self):
            """Returns tuple list of points between ends, inclusive. O(k) where k is pipe length"""
            #establish start and stop points
            xpos = min(self.x1,self.x2)
            ypos = min(self.y1,self.y2)
            xend = max(self.x1,self.x2)
            yend = max(self.y1,self.y2)
            points = [(xpos,ypos)]

            #add point, increment towards opposite end
            while (xpos != xend):
                xpos += 1
                points.append((xpos,ypos))
            while (ypos != yend):
                ypos += 1
                points.append((xpos,ypos))
            return points

        def is_straight(self) -> bool:
            """Returns true if the pipe is purely horizontal or vertical (not diagonal)"""
            return self.x1 == self.x2 or self.y1 == self.y2

    def __init__(self,file) -> None:
        """Takes file name to initialize PipeNetwork object"""
        self.pipes = []
        self.network = []
        data = open(file,'r').readlines()
        for line in data:
            #maybe update this eventually and implement diagonal pipes
            new_pipe = self.Pipe(line)
            if new_pipe.is_straight():
                self.pipes.append(self.Pipe(line))
        self.make_network()
        return

    def __str__(self) -> str:
        #TODO: include grid print out
        ret_str = str(self.pipes)
        for row in self.network:
            str_ints = [str(int) for int in row]
            ret_str += "\n" + " ".join(str_ints)
        return ret_str

    def __repr__(self) -> str:
        return str(self)

    def find_dims(self):
        """Helps initialize the network grid. Returns max x,y values. O(n)"""
        x,y = 0,0
        for p in self.pipes:
            #finds maximum x,y values in pipes list
            start,end = p.get_ends()
            if start[0] > x:
                x = start[0]
            elif end[0] > x:
                x = end[0]
            if start[1] > y:
                y = start[1]
            elif end[1] > y:
                y = end[1]
        return x,y

    def make_network(self) -> None:
        """ Makes network grid, iterates through pipes list and adds to network. 
        O(nk) where k is proportional to pipe length/grid dimensions"""
        x,y = self.find_dims()
        self.network = [[0]*(x+1) for n in range(y+1)] #create empty network grid

        for p in self.pipes:
            points = p.points_between()
            for x,y in points:
                self.network[y][x] += 1
        return

    def count_overlaps(self) -> int:
        """ Returns sum of overlaps. O(k^2), where k is related to pipe length/grid dimensions"""
        sum = 0
        for row in self.network:
            for x in row:
                if x > 1:
                    sum += 1
        return sum