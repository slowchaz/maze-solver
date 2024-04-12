from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
      self.__root = Tk()
      self.__root.title("Maze Runner")
      self.__canvas = Canvas(self.__root, width=width, height=height)
      self.__canvas.pack(fill=BOTH, expand=1)
      self.__running = False
      self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
      self.__root.update_idletasks()
      self.__root.update()

    def wait_for_close(self):
      self.__running = True
      while self.__running:
        self.redraw()

    def close(self):
      self.__running = False

    def draw_line(self, line, fill_color="black"):
      line.draw(self.__canvas, fill_color)
    
    def draw_cell(self, cell, fill_color="teal"):
      cell.draw(self.__canvas, fill_color)
      

class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y

class Line:
    def __init__(self, start, end):
      self.start = start
      self.end = end
    
    def draw(self, canvas, fill):
      canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill, width=2)
      canvas.pack(fill=BOTH, expand=1)

class Cell:
  def __init__(self, win):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._y1 = None
    self._x2 = None
    self._y2 = None
    self._win = win
  
  def draw(self, x1, y1, x2, y2):
    if self._win is None:
        return
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2

    top_left = Point(self._x1, self._y1)
    top_right = Point(self._x2, self._y1)
    bottom_right = Point(self._x2, self._y2)
    bottom_left = Point(self._x1, self._y2)

    left_wall = Line(bottom_left, top_left)
    right_wall = Line(top_right, bottom_right)
    top_wall = Line(top_left, top_right)
    bottom_wall = Line(bottom_right, bottom_left)

    if self.has_left_wall:
      self._win.draw_line(left_wall)
    else:
      self._win.draw_line(left_wall, "#ececec")
    if self.has_right_wall:
      self._win.draw_line(right_wall)
    else:
      self._win.draw_line(right_wall, "#ececec")
    if self.has_top_wall:
      self._win.draw_line(top_wall)
    else:
      self._win.draw_line(top_wall, "#ececec")
    if self.has_bottom_wall:
      self._win.draw_line(bottom_wall)
    else:
      self._win.draw_line(bottom_wall, "#ececec")


  def draw_move(self, to_cell, undo=False):
    if self._win is None:
      return
    
    color = "gray" if undo else "red"

    cell_one_x_center = (self._x1 + self._x2) / 2
    cell_one_y_center = (self._y1 + self._y2) / 2

    cell_two_x_center = (to_cell._x1 + to_cell._x2) / 2
    cell_two_y_center = (to_cell._y1 + to_cell._y2) / 2

    # line = Line(Point(cell_one_x_center, cell_one_y_center), Point(cell_two_x_center, cell_two_y_center))

    # self._win.draw_line(line, color)
    # moving left
    if self._x1 > to_cell._x1:
        line = Line(Point(self._x1, cell_one_y_center), Point(cell_one_x_center, cell_one_y_center))
        self._win.draw_line(line, color)
        line = Line(Point(cell_two_x_center, cell_two_y_center), Point(to_cell._x2, cell_two_y_center))
        self._win.draw_line(line, color)

    # moving right
    elif self._x1 < to_cell._x1:
        line = Line(Point(cell_one_x_center, cell_one_y_center), Point(self._x2, cell_one_y_center))
        self._win.draw_line(line, color)
        line = Line(Point(to_cell._x1, cell_two_y_center), Point(cell_two_x_center, cell_two_y_center))
        self._win.draw_line(line, color)

    # moving up
    elif self._y1 > to_cell._y1:
        line = Line(Point(cell_one_x_center, cell_one_y_center), Point(cell_one_x_center, self._y1))
        self._win.draw_line(line, color)
        line = Line(Point(cell_two_x_center, to_cell._y2), Point(cell_two_x_center, cell_two_y_center))
        self._win.draw_line(line, color)

    # moving down
    elif self._y1 < to_cell._y1:
        line = Line(Point(cell_one_x_center, cell_one_y_center), Point(cell_one_x_center, self._y2))
        self._win.draw_line(line, color)
        line = Line(Point(cell_two_x_center, cell_two_y_center), Point(cell_two_x_center, to_cell._y1))
        self._win.draw_line(line, color)

  def break_wall(self, wall):
    if wall == 0:
      self.has_left_wall = False
    elif wall == 1:
      self.has_right_wall = False
    elif wall == 2:
      self.has_top_wall = False
    elif wall == 3:
      self.has_bottom_wall = False
    else:
      raise ValueError("Invalid wall value")
    
