# Alex Zhu
# 12/12/21
# Advent of Code - DAY ONE

#Is this necessary? No, but it was fun
MOVES = {
    'forward' : lambda p,d : [p[0] + d, p[1], p[2]+p[1]*d],
    'up' : lambda p,d : [p[0], p[1] - d, p[2]],
    'down' : lambda p,d : [p[0], p[1] + d, p[2]]
}

def parser(file):
    """Parses provided text file. Returns list of tuples (dir,value). O(n)"""
    return list(map(lambda s : tuple(s.split()),open(file, 'r').readlines()))   #another one liner because I'm a menace

def i_like_to_move_it(lst):
    """Calculates final position based on given move list. O(n)"""
    pos = [0,0,0] #[x,y,aim]
    for move in lst:
        pos = MOVES[move[0]](pos,int(move[1]))
    return pos

if __name__ == "__main__":
    lst = parser("input.txt")
    pos = i_like_to_move_it(lst)
    print("PART ONE: [{0},{1}] : {2}".format(pos[0],pos[1],pos[0]*pos[1]))
    print("PART TWO: [{0},{1}] : {2}".format(pos[0],pos[2],pos[0]*pos[2]))
