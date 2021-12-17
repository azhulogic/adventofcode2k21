# Alex Zhu
# 12/14/21
# Advent of Code - DAY FIVE

from PipeNetwork import PipeNetwork

if __name__ == "__main__":
    print("[--EXAMPLE--]")
    exampleNetwork = PipeNetwork("example.txt")
    print(exampleNetwork)
    print("Overlaps:",exampleNetwork.count_overlaps())

    print("[--INPUT--]")
    network = PipeNetwork("input.txt")
    #do not print it out it's huge
    print("Overlaps:",network.count_overlaps())
    #print(exampleNetwork.find_dims())