from Square import Square
from Piece import Piece


class Board:
  def __init__(self):
    self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                  ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                  [".", ".", ".", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."],
                  [".", ".", ".", ".", ".", ".", ".", "."],
                  ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                  ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

  def is_square_empty(self, square):
    return self.board[square.row_index][square.column_index] == "."
  
  def square(self, square):
    if not self.is_square_empty(square):
      return Piece(self.board[square.row_index][square.column_index])
    else:
      return "."