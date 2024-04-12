from tkinter import Tk, BOTH, Canvas

def main():
    print("Hello!")
    win = Window(800, 600)
    win.wait_for_close()


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Default Title")
        self.__canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.__canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False



main()
