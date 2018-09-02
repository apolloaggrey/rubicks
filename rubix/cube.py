from face import *


class Cube(object):
    """docstring for Cube"""
    shades = {"W":"#feffe1","G":"#00ff00","R":"#FF0000","B":"#0000ff","Y":"#FFFF00","O":"#ff7a00",}

    def __init__(self, name=None):
        shades = {"W": "#feffe1", "G": "#00ff00", "R": "#FF0000", "B": "#0000ff", "Y": "#FFFF00", "O": "#ff7a00", }
        super(Cube, self).__init__()
        self.name = name
        self.back_face= Face()
        self.left_face = Face()
        self.top_face = Face()
        self.right_face = Face()
        self.front_face = Face()
        self.bottom_face = Face()

        # #################### TEMPORARY #########################
        self.back_face.center_row.squares[1].colour = "W"
        self.left_face.center_row.squares[1].colour = "G"
        self.top_face.center_row.squares[1].colour = "R"
        self.right_face.center_row.squares[1].colour = "B"
        self.front_face.center_row.squares[1].colour = "Y"
        self.bottom_face.center_row.squares[1].colour = "O"
        # ##################################################

        self.faces = [
            self.back_face,
            self.left_face,
            self.top_face,
            self.right_face,
            self.front_face,
            self.bottom_face]



    def __str__(self):
        string = ""
        for face in self.faces:
            for row in face.rows:
                string += str(row)
            string += "."
        return string

    def rotate_face(self, cube_face, clockwise=True):
        self.faces[cube_face].rotate()
        pass

    def rotate_cube(self, direction="(FRLBUDMN),(FRLBUDMN)'"):
        pass

    def scramble(self,sequence = None):# 20 random moves
        pass


def main():
    x = Cube("R")
    print(x)
    pass


if __name__ == '__main__':
    main()