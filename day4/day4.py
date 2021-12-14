# Alex Zhu
# 12/13/21
# Advent of Code - DAY FOUR

from Bingo import Bingo

if __name__ == "__main__":
    print("[--EXAMPLE--]")

    exgame = Bingo("example.txt")
    dub_board,x = exgame.play_bingo()
    sum = dub_board.unmarked_sum()
    print("Unmarked Sum:{0} - Winning Num:{1} - Product:{2}".format(sum,x,x*sum))

    l_board,x = exgame.lose_bingo()
    sum = l_board.unmarked_sum()
    print("Unmarked Sum:{0} - Winning Num:{1} - Product:{2}".format(sum,x,x*sum))

    print("\n[--INPUT--]")
    game = Bingo("input.txt")
    dub_board,x = game.play_bingo()
    sum = dub_board.unmarked_sum()
    print("Unmarked Sum:{0} - Winning Num:{1} - Product:{2}".format(sum,x,x*sum))

    l_board,x = game.lose_bingo()
    sum = l_board.unmarked_sum()
    print("Unmarked Sum:{0} - Winning Num:{1} - Product:{2}".format(sum,x,x*sum))