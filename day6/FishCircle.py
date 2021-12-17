# Alex Zhu
# 12/16/21
# Advent of Code - DAY SIX

class FishCircle:
    def __init__(self,file) -> None:
        """Initializes fish circle from file. O(n)"""
        f = open(file,'r')
        initial_fish = list(map(int,f.readline().split(','))) #int list representation of input string

        self.age_groups = [0]*9
        self.zero_age = 0

        for x in initial_fish:
            self.age_groups[x] += 1

    def __str__(self) -> str:
        zdx = self.zero_age
        ret_str = "FISH CIRCLE: ["
        for i in range(9):
            age = (zdx + i) % 9
            ret_str += "(age {0} : {1} fish), ".format(i,self.age_groups[age])
        return ret_str[:-2] + "]"

    def lifecycle(self,days) -> None:
        """Simulates lanternfish through lifecycles as per prompt. O(d) where d is days"""
        zdx = self.zero_age
        for i in range(days):
            self.age_groups[(zdx + 7) % 9] += self.age_groups[zdx]
            zdx = (zdx + 1) % 9
        self.zero_age = zdx

    def total_fish(self) -> int:
        """Counts total amount of fish. O(1), since list is fixed size"""
        return sum(self.age_groups)