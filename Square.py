class Square:
  def __init__(self, position):
    self.position = position
    self.column = position[0]
    self.row = position[1]
    
    # Convert to indices
    letters_to_numbers = {chr(97+x):x for x in range(8)}
    self.row_index = 8 - int(self.row)
    self.column_index = letters_to_numbers[self.column]