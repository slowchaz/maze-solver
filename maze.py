from graphics import Cell
import time, random

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self._create_cells()
  
  def _create_cells(self):
    for i in range(self._num_cols):
        col_cells = []
        for j in range(self._num_rows):
            col_cells.append(Cell(self._win))
        self._cells.append(col_cells)
    
    for i in range(self._num_cols):
        for j in range(self._num_rows):
            self._draw_cell(i, j)
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_visited()

  def _draw_cell(self, i, j):
    if self._win is None:
        return
    x = self._x1 + i * self._cell_size_x
    y = self._y1 + j * self._cell_size_y

    self._cells[i][j].draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
    self._animate()

  def _animate(self):
    if self._win is None:
        return
    self._win.redraw()
    time.sleep(0.025)
    
  def _break_entrance_and_exit(self):
    self._cells[0][0].break_wall(0)
    self._draw_cell(0, 0)

    self._cells[self._num_cols - 1][self._num_rows - 1].break_wall(1)
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True

    while True:
      to_visit = []

      if i > 0 and not self._cells[i - 1][j].visited:
          to_visit.append((i - 1, j, 0))  # North
      if j > 0 and not self._cells[i][j - 1].visited:
          to_visit.append((i, j - 1, 2))  # West
      if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
          to_visit.append((i + 1, j, 1))  # South
      if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
          to_visit.append((i, j + 1, 3))  # East

      if not to_visit:
          self._draw_cell(i, j)
          break

      ni, nj, direction = random.choice(to_visit) 

      # Break the wall between (i, j) and (ni, nj)
      if direction == 0:  # North
          self._cells[i][j].break_wall(0)
          self._cells[ni][nj].break_wall(1)
      elif direction == 1:  # South
          self._cells[i][j].break_wall(1)
          self._cells[ni][nj].break_wall(0)
      elif direction == 2:  # West
          self._cells[i][j].break_wall(2)
          self._cells[ni][nj].break_wall(3)
      else:  # East
          self._cells[i][j].break_wall(3)
          self._cells[ni][nj].break_wall(2)

      self._draw_cell(i, j)
      self._break_walls_r(ni, nj)

  def _reset_visited(self):
    for i in range(self._num_cols):
        for j in range(self._num_rows):
            self._cells[i][j].visited = False

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True

    if (self._cells[i][j] == self._cells[self._num_cols - 1][self._num_rows - 1]):
        return True

    # for each direction
    for direction in range(4):
        ni, nj = i, j  

        if direction == 0 and j > 0: # North
            ni, nj = i, j - 1
        elif direction == 1 and j < self._num_rows - 1: # South
            ni, nj = i, j + 1
        elif direction == 2 and i > 0: # West
            ni, nj = i - 1, j
        elif direction == 3 and i < self._num_cols - 1: # East
            ni, nj = i + 1, j
        else:
            continue  # Skip this iteration if out of bounds

        # Check if the cell can be moved into
        if not self._cells[ni][nj].visited and (direction == 0 and not self._cells[ni][nj].has_bottom_wall or
                                                direction == 1 and not self._cells[ni][nj].has_top_wall or
                                                direction == 2 and not self._cells[ni][nj].has_right_wall or
                                                direction == 3 and not self._cells[ni][nj].has_left_wall):
            self._cells[i][j].draw_move(self._cells[ni][nj])
            if self._solve_r(ni, nj):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)

    return False  # This should only be executed if all directions have been tried and failed
          

