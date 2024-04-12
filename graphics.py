from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
      self.__root = Tk()
      self.__root.title("Default Title")
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
    if self.has_right_wall:
      self._win.draw_line(right_wall)
    if self.has_top_wall:
      self._win.draw_line(top_wall)
    if self.has_bottom_wall:
      self._win.draw_line(bottom_wall)

    
