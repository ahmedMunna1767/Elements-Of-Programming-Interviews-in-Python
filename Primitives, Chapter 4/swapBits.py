PRECOMPUTED_REVERSE = {
    0: 0,
    1: 2,
    2: 1,
    3: 3
}

# complexity O(1)
def swap_bits(x, i, j):
    iBit = (x >> i) & 1
    jBit = (x >> j) & 1

    if iBit != jBit: 
        comp = (1 << i) | (1 << j)
        return x ^ comp
    return x

def reverse_bits(x: int) -> int:
    size = len(bin(x)) - 2
    print(bin(x))
    position = size - 1
    y = 0
    while position >= 0:
        y1 = (x  & 1) << position
        x = x >> 1
        y = y | y1
        position = position - 1
    print(bin(y))
    return y

""" def reverse(x : int) -> int:
    MASK_SIZE = 2
    BIT_MASK = 0b11
    no_of_chunks = 64 // MASK_SIZE
    result = 0
    for i in range(no_of_chunks):
        if i == 0:
            chunk_result = PRECOMPUTED_REVERSE[x & BIT_MASK]
        elif i == no_of_chunks:
            chunk_result = PRECOMPUTED_REVERSE[x >> (i * MASK_SIZE)]
        else:
            chunk_result = PRECOMPUTED_REVERSE[x >> (i * MASK_SIZE) & BIT_MASK]
        result = result ^ chunk_result
    return result
 """

# complexity O(wordSize)
def closest_int_same_bit_count (x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if (x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i + 1)) # Swaps bit-i and bit-(i + 1)
    return x
    raise ValueError('A1l bits are 0 or 1')

# complexity O(1)
def closest_int_same_bit_count_2 (x):
    print(bin(x))
    if not x&1:
        lowestSetBit = x & (~(x - 1))
        x = x & (x - 1)
        x = x ^ (lowestSetBit >> 1)
    else :
        firstZero = ~x & ~(~x - 1)
        x = x & (x - 1)
        x = x | firstZero
    print(bin(x))
    return x



if __name__ == '__main__':
    #print(bin(2), bin(swap_bits(2, 0, 1)))
    #print(bin(92),(closest_int_same_bit_count(92)))
    # reverse_bits(2056)
    closest_int_same_bit_count_2(0b10001000)
    closest_int_same_bit_count_2(0b10000111) 