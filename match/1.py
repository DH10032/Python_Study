'''
실행결과 : X=1
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(1, 0))
