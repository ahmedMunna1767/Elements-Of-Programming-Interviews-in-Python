PRECOMPUTED_PARITY = {
    0 : 0,
    1 : 1,
    2 : 1,
    3 : 0,
    4 : 1,
    5 : 0,
    6 : 0,
    7 : 1,
    8 : 1,
    9 : 0,
    10 : 0,
    11 : 1,
    12 : 0,
    13 : 1,
    14 : 1,
    15 : 0
}

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits = num_bits + (x & 1)
        x = x >> 1
    return num_bits

def run_count_bits():
    for i in range(20):
        print(i, count_bits(i))
""" 
even 1 --> 0
odd 1  --> 1
"""

# complexity O(n)
def parity_1(x : int) -> int:
    num_bits = count_bits(x=x)
    if num_bits % 2== 0:
        return 0
    else:
        return 1

def parity_2(x : int) -> int:
    result = 0
    while x:
        result = result ^ (x & 1)
        x = x >> 1

    return result 


# complexity O(k) k = number of set(1) bits
def parity_3(x : int) -> int:
    result = 0
    while x:
        result = result ^ 1
        x = x & (x - 1)
    
    return result

# complexity O(n / L) n = word size , L = MASK_SIZE
def parity_4(x : int) -> int:
    MASK_SIZE = 4
    BIT_MASK = 0xF
    no_of_chunks = 64 // MASK_SIZE
    result = 0
    for i in range(no_of_chunks):
        if i == 0:
            chunk_result = PRECOMPUTED_PARITY[x & BIT_MASK]
        elif i == no_of_chunks:
            chunk_result = PRECOMPUTED_PARITY[x >> (i * MASK_SIZE)]
        else:
            chunk_result = PRECOMPUTED_PARITY[x >> (i * MASK_SIZE) & BIT_MASK]
        result = result ^ chunk_result
    return result

# complexity O(logn) n = word size 
def parity_5(x : int) -> int:
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)

    return x & 0x1


def run_parity():
    for i in range(300000):
        a = parity_1(i)
        b = parity_2(i)
        c = parity_3(i)
        d = parity_4(i)
        e = parity_5(i)
        if not (a==b==c==d==e):
            print(i, a, b, c, d, a==b==c==d==e)
            return
    print("Test Successful")

if __name__ == '__main__':
    print("Program Running")
    run_parity()

    