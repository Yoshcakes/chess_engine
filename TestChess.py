import unittest
from ChessGame import ChessGame
from Board import Board
from Square import Square
from Move import Move
from Piece import Piece


class TestChess(unittest.TestCase):

  def testPieceSquares(self):
    game = ChessGame()
    self.assertEqual(game.board.square(Square("a1")), Piece("wR"))
    self.assertEqual(game.board.square(Square("d1")), Piece("wQ"))
    self.assertEqual(game.board.square(Square("d8")), Piece("bQ"))

  def testEmptySquares(self):
    game = ChessGame()
    self.assertEqual(game.board.is_square_empty(Square("b4")), True)
    self.assertEqual(game.board.square(Square("e4")), ".")
  
  def testPawnMove(self):
    game = ChessGame()
    game.play(Move(game.player, "e3"))
    self.assertEqual(game.board.square(Square("e2")), ".")
    self.assertEqual(game.board.square(Square("e3")), Piece("wP"))


if __name__ == '__main__':
  unittest.main()