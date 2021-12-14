# Alex Zhu
# 12/13/21
# Advent of Code - DAY FOUR

class Bingo:
    class Board:
        #a useful nested class for representing and manipulating bingo boards
        def __init__(self) -> None:
            board_arr = []

        def __init__(self, row_lst) -> None:
            self.row_lst = row_lst

        def __str__(self):
            """For print(), has decent formatting if no more than two digits. O(n^2)"""
            ret_str = ""
            for row in self.row_lst:
                for el in row:
                    if el < 0:
                        el_str = "{0}*".format(el)
                    else:
                        el_str = str(el)
                    ret_str += "{0:<3} ".format(el_str)
                ret_str += "\n"
            return ret_str

        def __repr__(self):
            return str(self)

        def set_elem(self,x,y):
            pass

        def get_elem(self,x,y):
            pass

        def find_elem(self,el):
            return (x,y)

        def negate_elem(self,el):
            pass

    def __init__(self, file) -> None:
        """Constructor for Bingo game, takes file name as input. O(n)"""
        f = open(file,'r')
        self.nums = list(map(int,f.readline().split(','))) #instructions as int list

        #instantiate all the given boards as Board objects
        f.readline() #need to skip a line
        board_strs = f.readlines()
        self.boards = []
        curr_board = []

        for str in board_strs:
            str.strip('\n')
            if str != "":
                lst = map(int,str.split())
                curr_board.append(lst)
            else:
                self.boards.append(self.Board(curr_board))
                curr_board = []
        self.boards.append(self.Board(curr_board))

        print(self.boards[0])
        print(self.nums)
    
    def mark_boards(self):
        pass