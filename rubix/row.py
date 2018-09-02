from square import *


class Row(object):
    """docstring for Raw"""

    def __init__(self, colours=None):
        super(Row, self).__init__()
        if type(colours) == list:
            self.left_square = Square(colours[0])
            self.center_square = Square(colours[1])
            self.right_square = Square(colours[2])
            self.squares = [self.left_square, self.center_square, self.right_square]
        else:
            self.left_square = Square(colours)
            self.center_square = Square(colours)
            self.right_square = Square(colours)
            self.squares = [self.left_square, self.center_square, self.right_square]

    def __str__(self):
        string = ""
        for square in self.squares:
            string += str(square)
        return string

    def list_to_Row(self, list):
        x = Row()
        x.left_square = Square(list[0])
        x.center_square = Square(list[1])
        x.right_square = Square(list[2])
        x.squares = [x.left_square, x.center_square, x.right_square]
        return x


def main():
    x = Row("R")
    print(x)
    pass


if __name__ == '__main__':
    main()
