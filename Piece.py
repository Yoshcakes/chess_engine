class Piece:
  def __init__(self, piece):
    self.color = piece[0]
    self.piece = piece[1]

  def __eq__(self, other):
    return self.__dict__ == other.__dict__