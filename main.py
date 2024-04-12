from graphics import Window, Point, Line

def main():
    print("Hello!")
    win = Window(800, 600)

    point_start = Point(0, 0)
    point_end = Point(150, 150)

    line = Line(point_start, point_end)

    win.draw_line(line, "teal")

    point_start = Point(150, 150)
    point_end = Point(0, 300)

    line = Line(point_start, point_end)

    win.draw_line(line, "teal")

    win.wait_for_close()
    print("Goodbye!")

main()
