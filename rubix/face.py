from row import *


class Face(object):
    """docstring for Face"""

    def __init__(self, colour=None):
        super(Face, self).__init__()
        self.top_row = Row(colour)
        self.center_row = Row(colour)
        self.bottom_row = Row(colour)
        self.rows = [self.top_row, self.center_row, self.bottom_row]
        self.colour = str(self)[4]

    def __str__(self):
        string = ""
        for row in self.rows:
            string += str(row) + "\n"
        return string

    def colour(self):
        return self.center_row.squares[1].colour

    def rotate(self, clockwise=True):  # Todo
        if clockwise:
            for x in range(2):
                s0 = []
                for row in self.rows:
                    s0 += str(row)
                s = s0
                temp = s[0]
                s[0] = s[3]
                s[3] = s[6]
                s[6] = s[7]
                s[7] = s[8]
                s[8] = s[5]
                s[5] = s[2]
                s[2] = s[1]
                s[1] = temp
                self.list_to_face(s)
            pass
        else:
            for x in range(3):
                self.rotate()
            pass

    def list_to_face(self, list):
        self.top_row = Row(list[0:3])
        self.center_row = Row(list[3:6])
        self.bottom_row = Row(list[6:9])
        self.rows = [self.top_row, self.center_row, self.bottom_row]
        self.colour = self.center_row.center_square.colour
        pass


def main():
    x = Face()
    print(x)
    x.rotate(False)
    print(x)
    x.rotate()
    print(x)
    pass


if __name__ == '__main__':
    main()
