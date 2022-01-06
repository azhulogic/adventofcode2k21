# Alex Zhu
# 12/30/21
# Advent of Code - DAY NINE

from HeightMap import HeightMap

if __name__ == "__main__":
    ex = HeightMap("example.txt")
    print(ex)
    print(ex.find_low_points())
    print("Risk Level Sum: {0}".format(ex.risk_level()))

    ex2 = HeightMap("example2.txt")
    print(ex2)
    print(ex2.find_low_points())
    #print("Risk Level Sum: {0}".format(ex2.risk_level()))

    ex3 = HeightMap("example3.txt")
    print(ex3)
    print(ex3.find_low_points())
    #print("Risk Level Sum: {0}".format(ex3.risk_level()))

    hm_one = HeightMap("input.txt")
    #print(hm_one)
    print()
    #print(hm_one.find_low_points())
    print(hm_one.risk_level())