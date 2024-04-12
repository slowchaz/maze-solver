from graphics import Window, Cell
from maze import Maze

def main():
    print("Hello!")
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 10, 50, 50, win)

    win.wait_for_close()
    print("Goodbye!")

main()
