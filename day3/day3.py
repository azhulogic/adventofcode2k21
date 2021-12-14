# Alex Zhu
# 12/13/21
# Advent of Code - DAY THREE

#I don't love my solution for this, feels like it could be much cleaner
#but I got to the point where I just wanted to be done and refactoring was not worth it
#might consider switching over to Java for future problems, either way switch to OOP
import copy

def parser(file):
    """Parser, returns list of int lists representing binary sequences. O(n)"""
    return list(map(list,map(lambda s : list(map(int,s.strip())),open(file,'r').readlines()))) #my most horrific one liner yet, and yet so beautiful

def to_bit_or_not_to_bit(lst):
    """Counts bits by position, returns list with each position containing the most common bit. O(l*n) where l is the bit length"""
    #sum up each position
    common_lst = [0] * len(lst[0])
    for bit_lst in lst:
        for idx in range(len(bit_lst)):
            common_lst[idx] += bit_lst[idx]

    #set each position to most common bit, kind of confusing
    #greater than or equal to half the total numbers => 1 is more common
    half = len(lst)//2 + len(lst)%2 #this has to be like this because I'm bad at coding
    for idx in range(len(common_lst)):
        common_lst[idx] = int(common_lst[idx] >= half)
    return common_lst

def invert(bit_lst):
    """Inverts a  bit list, technically modifies . O(n)"""
    #which solution do you like more?
    #return list(map(lambda x : (x+1)%2, bit_lst))
    return list(map(lambda x : int(not x), bit_lst))    

def bit_to_num(bit_lst):
    """Converts binary representation int list into decimal. O(n)"""
    n = len(bit_lst)
    sum = 0

    for idx in range(n):
        if bit_lst[idx]:
            sum += 2**(n-idx-1) #invert index and sum powers of 2
    return sum

def epsilon_gamma(g_lst):
    """Returns (epsilon,gamma) tuple as per prompt. O(n)"""
    e_lst = invert(g_lst)
    gamma = bit_to_num(g_lst)
    epsilon = bit_to_num(e_lst)

    print("Epsilon: {0} -> {2}\nGamma:   {1} -> {3}".format(g_lst,e_lst,gamma,epsilon))   #useful debugging
    print("Power Consumption: {0}".format(gamma*epsilon))
    return (epsilon,gamma)

def ratings(bit,idx,lst):
    """Helper for o2_co2(). O(n)"""
    #print(lst)
    #print("Current common:{0}".format(to_bit_or_not_to_bit(lst)))
    #print("Looking for:{0} at:{1} in {2}".format(bit,idx,lst))
    if len(lst) > 1:
        return [x for x in lst if x[idx]==bit]
    else:
        return lst

def o2_co2(lst):
    """ Returns (oxygen,co2) ratings based on prompt algorithm. O(l*n) where l is bit length
        Needs a little bit of work ngl"""
    o2_lst = copy.deepcopy(lst)
    co2_lst = copy.deepcopy(lst)

    #See helper function above, iteratively removes elements from the list
    #I'm sure there's a more clever solution though
    for idx in range(len(common_lst)):
        bit = to_bit_or_not_to_bit(o2_lst)[idx]
        o2_lst = ratings(bit,idx,o2_lst)
        bit = invert(to_bit_or_not_to_bit(co2_lst))[idx]
        co2_lst = ratings(bit,idx,co2_lst)
    o2_rating = bit_to_num(o2_lst[0])
    co2_rating = bit_to_num(co2_lst[0])

    print("O2: {0} -> {2}\nCO2:  {1} -> {3}".format(o2_lst,co2_lst,o2_rating,co2_rating))   #useful debugging
    print("Life Support Rating: {0}".format(o2_rating*co2_rating))
    return (o2_rating,co2_rating)


if __name__ == "__main__":
    print("[--EXAMPLE--]")
    lst = parser("example.txt")
    common_lst = to_bit_or_not_to_bit(lst)
    e,g = epsilon_gamma(common_lst)
    o2,co2 = o2_co2(lst)

    print("[--INPUT--]")
    lst = parser("input.txt")
    common_lst = to_bit_or_not_to_bit(lst)
    e,g = epsilon_gamma(common_lst)
    o2,co2 = o2_co2(lst)
