import collections
import math
from typing import Type


def reverse_digit(x : int) -> int:
    result, x_remaining = 0, abs(x)

    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining = x_remaining // 10

    return -result if x < 0 else result


def is_palindrome(x : int) -> bool:
    if x <= 0:
        return x == 0

    num_of_digits = math.floor(math.log10(x)) + 1

    msd_mask = 10**(num_of_digits - 1)

    for i in range(num_of_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x = x % msd_mask
        x = x // 10
        msd_mask = msd_mask // 100

    return True

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

def intersect_rectangle(R1, R2):
    def is_intersect(R1, R2) :
        return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x
                    and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1) # IVo intersection.
    
    return Rectangle(max(R1. x , R2. x), max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))

def intersect_rectangle_2(R1: Type[Rectangle], R2: Type[Rectangle]) -> Type[Rectangle]:
    leftX, rightX, topY, bottomY = 0, 0, 0, 0

    leftX = max(R1.x, R2.x)
    topY = max(R1.y, R2.y)
    rightX = min(R1.x + R1.width, R2.x + R2.width)
    bottomY = min(R1.y + R1.height, R2.y + R2.height)

    if (leftX <= rightX) and (topY <= bottomY):
        return Rectangle(leftX, topY, rightX - leftX, bottomY - topY)
    else:
        return Rectangle(0, 0, -1, -1)





def uniforrn_random(lower_bound: int, upper_bound: int):
    pass

if __name__ == '__main__':
    print(reverse_digit(123456))
    print(reverse_digit(-123456))

    print(is_palindrome(123456))
    print(is_palindrome(123321))

    R1 = Rectangle(0, 0, 10, 10)
    R2 = Rectangle(5, 5, 10, 10)
    R3 = Rectangle(11, 11, 10, 10)
    R4 = Rectangle(10, 10, 10, 10)


    print(intersect_rectangle(R1=R1, R2= R2))
    print(intersect_rectangle_2(R1=R1, R2= R2))

    print(intersect_rectangle(R1=R1, R2= R4))
    print(intersect_rectangle_2(R1=R1, R2= R4))



    print(intersect_rectangle(R1=R1, R2= R3))
    print(intersect_rectangle_2(R1=R1, R2= R3))






