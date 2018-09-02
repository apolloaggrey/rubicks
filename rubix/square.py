import  random
class Square(object):
    """docstring for Square"""

    def __init__(self, colour=None):
        super(Square, self).__init__()
        if colour is None:
            colour = random.choice("WGRBYO")
        self.colour = colour

    def __str__(self):
        return f"{self.colour}"

def main():
    x = Square("R")
    print(x)
    pass


if __name__ == '__main__':
    main()