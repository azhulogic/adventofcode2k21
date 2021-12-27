# Alex Zhu
# 12/23/21
# Advent of Code - DAY EIGHT

class SevenSegment:
    class Number:
        #[a,b,c,d,e,f,g] by 'true' position
        #[0,1,2,3,4,5,6] by index
        NUMS = {
            "ZERO" : [1,1,1,0,1,1,1], #6 (1)
            "ONE"  : [0,0,1,0,0,1,0], #2 (2)
            "TWO"  : [1,0,1,1,1,0,1], #5 (1)
            "THREE": [1,0,1,1,0,1,1], #5 (2)
            "FOUR" : [0,1,1,1,0,1,0], #4 (1)
            "FIVE" : [1,1,0,1,0,1,1], #5 (3)
            "SIX"  : [1,1,0,1,1,1,1], #6 (2)
            "SEVEN": [1,0,1,0,0,1,0], #3 (1)
            "EIGHT": [1,1,1,1,1,1,1], #7 (1)
            "NINE" : [1,1,1,1,0,1,1]  #6 (3)
        }

        SEGS = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6}

        SEG_ON =  [" aaaa \n", "b    ", "c\n", " dddd \n", "e    ", "f\n", " gggg \n"]
        SEG_OFF = [" .... \n", ".    ", ".\n", " .... \n", ".    ", ".\n", " .... \n"]

        def __init__(self) -> None:
            self.seven_seg = [0] * 7

        def __init__(self,num) -> None:
            self.seven_seg = self.NUMS[num]

        def __str__(self) -> str:
            segs = []

            for i in range(len(self.seven_seg)):
                if self.seven_seg[i]:
                    segs.append(self.SEG_ON[i])
                else:
                    segs.append(self.SEG_OFF[i])

            return segs[0] + (segs[1]+segs[2])*4 + segs[3] + (segs[4]+segs[5])*4 + segs[6]

    def __init__(self,file) -> None:
        lines = open(file,'r').readlines()
        self.patterns = [""]*len(lines)
        self.outputs = [""]*len(lines)

        for i in range(len(lines)):
            split = lines[i].split(" | ")
            self.patterns[i] = split[0].split()
            self.outputs[i] = split[1].split()

    def __str__(self) -> str:
        out = ""

        for i in range(len(self.patterns)):
            out += str(self.patterns[i]) + " | \n" + str(self.outputs[i]) + "\n"

        return out

    def count_unique(self) -> int:
        """Counts unique outputs, 1,4,7,8. O(n)"""
        count = 0

        for lst in self.outputs:
            for item in lst:
                l = len(item)
                if l == 2 or l == 3 or l == 4 or l == 7:
                    count += 1
        
        return count

    #Logical rules for determining display
    # only (1),(4),(7) and (8) have unique char counts
    # non-unique char counts:
    ## 5-chars -> (2),(3),(5)
    ## 6-chars -> (0),(6),(9)
    # numbers with respective position
    ## pos 'a' -> (0),(2),(3),(5),(6),(7),(8),(9)
    ## pos 'b' -> (0),(4),(5),(6),(8),(9)
    ## pos 'c' -> (0),(1),(2),(3),(4),(7),(8),(9)
    ## pos 'd' -> (2),(3),(4),(5),(6),(8),(9)
    ## pos 'e' -> (0),(2),(6),(8)
    ## pos 'f' -> (0),(1),(3),(4),(5),(6),(7),(8),(9)
    ## pos 'g' -> (0),(2),(3),(5),(6),(8),(9)
    # the char not found in (1) from (7) must be pos 'a'
    ## from above: (2),(3),(5),(6) must have a pos 'a'
    # the char shared by (6) and the two-char (1) must be pos 'f'
    # the char shared by (5) and the two-char (1) must be pos 'f'
    # the char shared by (2) and the two-char (1) must be pos 'c'
    # the common char between (4) and (3) not included (1) must be pos 'd'
    # the two chars not shared by the two-char (1) and the four-char (4) must be pos 'b' or 'd'
    # the seven-char (8) is useless

    #idk where to declare this, but I imagine I'll eventually want a dictionary
    #where key is the input char, and value is the "correct" position definition
    #and using logic above can slowly fill this out
    CHAR_PAIR_DICT = {
        'a' : '',
        'b' : '',
        'c' : '',
        'd' : '',
        'e' : '',
        'f' : '',
        'g' : ''
    }

    def find(self, strlst, length): 
        """Find all strings with input length. O(n)"""
        pass