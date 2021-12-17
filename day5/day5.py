# Alex Zhu
# 12/14/21
# Advent of Code - DAY FIVE

from PipeNetwork import PipeNetwork

if __name__ == "__main__":
    # p1 = PipeNetwork.Pipe("1,1 -> 3,3")
    # p2 = PipeNetwork.Pipe("9,7 -> 7,9")
    # print(p1.points_between45())
    # print(p2.points_between45())

    print("[--EXAMPLE--]")
    exampleNetwork = PipeNetwork("example.txt")
    print(exampleNetwork)
    print("Overlaps:",exampleNetwork.count_overlaps())

    print("[--INPUT--]")
    network = PipeNetwork("input.txt")
    #do not print it out it's huge
    print("Overlaps:",network.count_overlaps())
    #print(exampleNetwork.find_dims())