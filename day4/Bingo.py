# Alex Zhu
# 12/13/21
# Advent of Code - DAY FOUR

class Bingo:
    class Board:
        #a useful nested class for representing and manipulating individual bingo boards
        def __init__(self, row_lst) -> None:
            self.row_lst = row_lst

        def __str__(self) -> str:
            """For print(), has decent formatting if no more than two digits. O(1) technically?"""
            ret_str = ""
            for row in self.row_lst:
                for el in row:
                    if el < 0:
                        el_str = "{0}*".format(-el)
                    else:
                        el_str = str(el)
                    ret_str += "{0:<3} ".format(el_str)
                ret_str += "\n"
            return ret_str

        def __repr__(self) -> str:
            return str(self)

        def set_elem(self,x,y,elem) -> None:
            """Set element by indexes"""
            self.row_lst[y][x] = elem

        def get_elem(self,x,y) -> int:
            """Return element by indexes"""
            return self.row_lst[y][x]

        def find_elem(self,el) -> tuple[int, int]:
            """Find if element exists on board, return its indexes or (-1,-1) if not found. 
            O(1), technically"""
            for y in range(len(self.row_lst)):
                row = self.row_lst[y]
                for x in range(len(row)):
                    if row[x] == el:
                        return (x,y)
            return (-1,-1)

        def mark(self,elem) -> None:
            """Basically just turns the specific element negative ("marks" it). O(1)"""
            x,y = self.find_elem(elem)
            if x != -1:
                el = self.row_lst[y][x]
                if el == 0:
                    #ugly special case with this method, but isn't pertinent later
                    self.set_elem(x,y,-1)
                else:
                    self.set_elem(x,y,-self.row_lst[y][x])

        def check_win(self) -> bool:
            """Checks if this board has a win. Technically runs O(1) with constant board size?
                A better implementation might be possible with a helper function, but this works"""
            #cases: 5 rows, 5 columns, no diagonals
            for idx in range(5):
                for jdx in range(5):
                    #check rows
                    if self.row_lst[idx][jdx] >= 0:
                        break
                    elif jdx == 4:
                        return True
                for jdx in range(5):
                    #check columns
                    if self.row_lst[jdx][idx] >= 0:
                        break
                    elif jdx == 4:
                        return True
            return False

        def unmarked_sum(self) -> int:
            """Returns sum of all unmarked elements. Technically O(1)"""
            sum = 0
            for row in self.row_lst:
                for element in row:
                    if element > 0:
                        sum += element
            return sum

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
            str = str.strip('\n')
            if str != "":
                lst = list(map(int,str.split()))
                curr_board.append(lst)
            else:
                nboard = self.Board(curr_board)
                self.boards.append(nboard)
                curr_board = []
        nboard = self.Board(curr_board)
        self.boards.append(nboard)
    
    def __str__(self) -> str:
        ret_str = "Instruction List: {0}\nBoards:\n".format(self.nums)
        for board in self.boards:
            ret_str += str(board) + "\n"
        return ret_str
    
    def mark_boards(self,num) -> None:
        """Marks boards with given num. O(b) where b is amount of boards"""
        for board in self.boards:
            board.mark(num)

    def is_winner(self):
        """Checks if there are any winning boards. O(n)"""
        for board in self.boards:
            if board.check_win():
                return board
        return None

    def play_bingo(self) -> int:
        """Plays bingo, returns a winning board and the winning number. O(nb) where b is amount of boards"""
        for x in self.nums:
            self.mark_boards(x)
            winner = self.is_winner()
            if winner:
                print("BINGO! @ Board {0} on #{1}!\n{2}".format(self.boards.index(winner)+1,x,winner))
                return winner, x
    
    def lose_bingo(self):
        """Finds last bingo board to win."""
        win_count = 0
        for x in self.nums:
            self.mark_boards(x)
            winner = self.is_winner()
            while winner:
                if len(self.boards) == 1:
                    print("\nLAST BINGO! On #{0}!\n{1}".format(x,winner))
                    return winner, x
                else:
                    self.boards.remove(winner)
                    win_count += 1
                    winner = self.is_winner()
        print("No winner found")
        return None, None