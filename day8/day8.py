# Alex Zhu
# 12/23/21
# Advent of Code - DAY EIGHT

from SevenSegment import SevenSegment

def test_nums():
    nums = ["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    for n in nums:
        print(SevenSegment.Number(n))

if __name__ == "__main__":
    #test_nums() #tests the print function for numbers
    #EXAMPLEs
    ex1 = SevenSegment("example.txt")
    print(ex1.count_unique())

    ex2 = SevenSegment("example2.txt")
    print(ex2.count_unique())

    #INPUT
    input = SevenSegment("input.txt")
    print(input.count_unique())