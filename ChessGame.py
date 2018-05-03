from Board import Board

class ChessGame:
  def __init__(self):
    self.board = Board()
    self.player = "w"

  def play(self, move):
    # Pawn
    currentSquare = move.currentSquare()
    futureSquare = move.futureSquare()
    self.board.board[currentSquare.row_index][currentSquare.column_index] = "."
    self.board.board[futureSquare.row_index][futureSquare.column_index] = move.piece()
    if self.player == "w": 
      self.player = "b"
    else:
      self.player = "w"
    return self

