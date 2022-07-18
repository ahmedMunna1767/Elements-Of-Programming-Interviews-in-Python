def add_bitwise(x: int, y: int): 
    carry = x & y 
    result = x ^ y
    if carry == 0:
        return result
    else:
        return add_bitwise(result, carry << 1)

def multiply(x: int, y: int) -> int:
    result = 0
    while x:
        if x & 1:
            result = add_bitwise(result, y)
        x = x >> 1
        y = y << 1
    return result

if __name__ == '__main__':
    print(multiply(13, 9))
    print(multiply(91, 131))
    print(multiply(10, 20))


    print(add_bitwise(20, 10))

