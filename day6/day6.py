# Alex Zhu
# 12/16/21
# Advent of Code - DAY SIX

#the obvious implementation is deceptive and I can already
#tell from the input that it will become far too memory
#expensive far too quickly

#perhaps a FIFO queue? otherwise a simple list
#perhaps the most sensible is a fixed-length circular array queue
#but I think linear is easier to implement without fancy
#indexing math

#FUCK IT WE'RE DOING BOTH

#basic linked list queue structure layout
# FRONT -> [age 0] -> [age 1] -> [age 2] -> [age 3] -> [age 4] -> [age 5] -> [age 6] -> [age 7] -> [age 8] <- REAR
# after being initialized, shouldn't ever change size, which is why a fixed-space might be better

#a better fixed list circular style
# [0,1,2,3,4,5,6,7,8] w/ "zero_age" index, a counting variable which shifts by one each cycle
# much better solution, me likey

from FishQueue import FishQueue
from FishCircle import FishCircle

if __name__ == "__main__":
    print("\n[--EXAMPLE--]")
    #Queue implementation
    example_school = FishQueue("example.txt")
    print("INITIAL",example_school)

    example_school.lifecycle(18)
    print("AFTER 18 DAYS",example_school)
    print("TOTAL:",example_school.total_fish())

    example_school.lifecycle(62)
    print("AFTER 80 DAYS",example_school)
    print("TOTAL:",example_school.total_fish(),"\n")

    #Circular list implementation
    example_school = FishCircle("example.txt")
    print("INITIAL",example_school)

    example_school.lifecycle(18)
    print("AFTER 18 DAYS",example_school)
    print("TOTAL:",example_school.total_fish())

    example_school.lifecycle(62)
    print("AFTER 80 DAYS",example_school)
    print("TOTAL:",example_school.total_fish(),"\n")  

    print("\n[--INPUT--]")
    #Queue
    school_of_fish = FishQueue("input.txt")
    school_of_fish.lifecycle(80)
    print("AFTER 80 DAYS",school_of_fish)
    print("TOTAL:",school_of_fish.total_fish())
    school_of_fish.lifecycle(256-80)
    print("TOTAL AFTER 256:",school_of_fish.total_fish())

    #Circle
    school_of_fish = FishCircle("input.txt")
    school_of_fish.lifecycle(80)
    print("AFTER 80 DAYS",school_of_fish)
    print("TOTAL:",school_of_fish.total_fish())
    school_of_fish.lifecycle(256-80)
    print("TOTAL AFTER 256:",school_of_fish.total_fish())