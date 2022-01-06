# Alex Zhu
# 12/30/21
# Advent of Code - DAY NINE

class HeightMap:
    def __init__(self,file) -> None:
        """Parses input, stores width and height"""
        f = open(file,'r')
        lines = f.readlines()
        self.grid = []

        for line in lines:
            self.grid.append([int(char) for char in line.replace('\n','')])

        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def __str__(self) -> str:
        ret_str = "\n{0}x{1} GRID\n".format(self.width,self.height) + "-"*self.width + "\n"
        for row in self.grid:
            for num in row:
                ret_str += str(num)
            ret_str += "\n"
        return ret_str

    def find_low_points(self):
        low_points = []
        for y in range(self.height):
            for x in range(self.width):
                if x-1 >= 0:
                    left = self.grid[y][x-1]
                else:
                    left = 10
                if x+1 < self.width:
                    right = self.grid[y][x+1]
                else:
                    right = 10
                if y-1 >= 0:
                    up = self.grid[y-1][x]
                else:
                    up = 10
                if y+1 < self.height:
                    down = self.grid[y+1][x]
                else:
                    down = 10

                num = self.grid[y][x]
                #print("[{0},{1},{2},{3}] : {4} at ({5},{6})".format(up,down,left,right,num,x,y))
                if left > num and right > num and up > num and down > num:
                    #print("found [{0},{1}]".format(x,y))
                    low_points.append(num)

        return low_points

    def risk_level(self):
        lps = self.find_low_points()
        return sum(lps) + len(lps)