# Alex Zhu
# 12/12/21
# Advent of Code - DAY ONE

def parser(file):
    """Parses provided text file. O(n)"""
    return list(map(int,open(file,'r').readlines()))  #open/reads input, maps string list->int list, is one line because funny

def we_have_to_go_deeper(lst):
    """Finds number of adjacent increases in depth in a given list. O(n)"""
    count = 0
    for idx in range(0,len(lst)-1):
        if lst[idx] < lst[idx+1]:
            count += 1
    return count

def sum3(lst,idx):
    """Helper for func below, sums 3 from list at given index. Throws error if OOB. O(1)"""
    try:
        return lst[idx]+lst[idx+1]+lst[idx+2]
    except IndexError:
        print("you done messed up")     #boi

def even_deeper_than_before(lst):
    """Counts number of adjacent three-measurement windows. O(n)"""
    mod_len = len(lst)-2                #useful param for next couple operations
    mod_lst = [0] * mod_len             #ever wish this was MATLAB?
    if (mod_len < 1):
        raise ValueError("Bad input!")  #error checking bcuz ima good boy
    for idx in range(0,mod_len):
        mod_lst[idx] = sum3(lst,idx)
    return we_have_to_go_deeper(mod_lst)

if __name__ == "__main__":
    lst = parser("input.txt")
    print("PART ONE: " + str(we_have_to_go_deeper(lst)))
    lst = parser("input2.txt")
    print("PART TWO: " + str(even_deeper_than_before(lst)))