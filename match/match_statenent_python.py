'''
C에서 많이 사용해온 switch 문법과 굉장히 유사하다.
실행결과 : x = 1, y = 1
'''

point = (1, 2)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
