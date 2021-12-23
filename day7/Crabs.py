# Alex Zhu
# 12/23/21
# Advent of Code - DAY SEVEN

class Crabs:
    def __init__(self,file) -> None:
        """Initializes Crab object from file name, only handles part two fuel case"""
        f = open(file,'r')
        self.nums = list(map(int,f.readline().split(',')))
        self.min = min(self.nums)
        self.max = max(self.nums)

        self.fuel_costs = [0]*(self.max-self.min+1)
        for i in range(1,len(self.fuel_costs)):
            self.fuel_costs[i] = self.fuel_costs[i-1] + i
    
    def sum_cost(self,n) -> int:
        """Helper function for below"""
        sum = 0
        for x in self.nums:
            sum += self.fuel_costs[abs(x-n)]
        return sum

    def sum_all(self):
        """Finds and returns minimum fuel cost and the position"""
        check_nums = range(self.min, self.max)
        sums = [0]*len(check_nums)
        for n in check_nums:
            sums[n-self.min] = self.sum_cost(n)
        min_sum = min(sums)
        return min_sum, check_nums[sums.index(min_sum)]