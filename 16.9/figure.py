class Triangle():
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def __str__(self):
        return f'Triangle({self.a}, {self.b}, {self.c}, {self.h})'

triangle1 = Triangle(3,4,5,4)
print(triangle1)