from Square import Square
from Piece import Piece


class Move:
  def __init__(self, player, move):
    self.player = player
    self.move = move

  def piece(self):
    # Pawn
    if self.move[0] in [chr(97+x) for x in range(8)]:
      return Piece(self.player + "P")
    # Rook
    if self.move[0] == "R":
      return Piece(self.player + "R")
    # Knight
    if self.move[0] == "N":
      return Piece(self.player + "N")
    # Bishop
    if self.move[0] == "B":
      return Piece(self.player + "B")
    # Queen
    if self.move[0] == "Q":
      return Piece(self.player + "Q")
    # King
    if self.move[0] == "K":
      return Piece(self.player + "K")

  def currentSquare(self):
    # Pawn
    return Square(self.move[-2] + str(int(self.move[-1]) - 1))

  def futureSquare(self):
    return Square(self.move[-2:])