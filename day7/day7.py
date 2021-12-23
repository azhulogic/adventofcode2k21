# Alex Zhu
# 12/23/21
# Advent of Code - DAY SEVEN

from Crabs import Crabs

if __name__ == "__main__":
    example_crab = Crabs("example.txt")
    print(example_crab.sum_all())

    crab = Crabs("input.txt")
    print(crab.sum_all())