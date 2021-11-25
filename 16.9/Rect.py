class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rec_perim(self):
        return 2 * (self.length + self.width)

rec1 = Rectangle(6,10)
print(rec1.rec_perim())