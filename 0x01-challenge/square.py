#!/usr/bin/python3
"""Class square """


class square:
    """ Documentation """
    width = 0

    def __init__(self, size=0):
        """ Documentation """
        self.width = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeterOfMySquare(self):
        """ Documentation """
        return (self.width * 4)

    def __str__(self):
        """ Documentation """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeterOfMySquare())
