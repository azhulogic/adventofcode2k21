# Alex Zhu
# 11/21/22
# Advent of Code - DAY TEN

#we're back because why not?
#warming up for this year
#also back to one file because I think it helps readability

#we're going to use a stack implementation
#class name is pormanteau of the words syntax and stack... synstax!! Get it??
class Synstax:
    SCORE_TABLE = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137
    }

    OPEN = ['(','[','{','<']
    CLOSE = [')',']','}','>']

    def __init__(self,file) -> None:
        """Parses input as a list of strings, initializes stack. O(n)"""
        with open(file,'r') as f:
            self.input = f.readlines()
        self.stack = []
        self.score = 0

    def __str__(self) -> str:
        """__str__ method"""
        print("Input is " + str(len(self.input)) + " rows long")
        print("Score found was:")
        print(self.score)

    #stack methods!
    # okay so admittedly python lists already come with these implementations
    # but for the sake of practice..
    def isEmpty(self) -> bool:
        """Self explanatory, hopefully. O(1)"""
        return len(self.stack == 0)

    def pop(self) -> char:
        """Return the top value with removal. O(1) amortized"""
        if isEmpty():
            raise AttributeError
            return None
        return self.stack.pop()

    def push(self, c) -> None:
        """Push new value onto stack. O(1) amortized"""
        self.stack.append(c)
    
    def peek(self) -> char:
        """Return the top value without removal. O(1)"""
        if isEmpty():
            return None
        return self.stack[-1]

    #syntax checking methods!
    def check_row(row) -> int:
        """Helper function for below, checks one row. O(n)
           ONLY checks for errors, not incompletions"""
        print_errors = True #change as needed

        #basically, push open brackets onto the stack
        #pop them off as matching closing brackets are found
        #if the top open bracket doesn't match the closing
        #bracket, then an error has occured..
        #thus return the score for that error
        for c in row:
            if c in OPEN:
                self.stack.push(c)
            elif c in CLOSE:
                top = self.stack.pop()
                if c != top or self.stack.isEmpty()
                    print("Expected to close " + c + " but saw " + top + "instead.")
                    return SCORE_TABLE[c]
            else:
                print("Unexpected character")
                raise ValueError
            

    def parse_lines() -> None:
        """Count syntax errors score from all rows of input. O(l*n) where l is avg line length and n is input length"""
        for row in self.input():
            try:
                self.score += check_row(row)
            except ValueError:
                print("Error:")

if __name__ == "__main__":
    example = Synstax("example.txt")
    example.parse_lines()
    print(example)