# Practice Challenges of 4.1

def power_of_two(x: int) -> bool:
    return (bool(x) and (not bool(x & (x - 1))))

def mod_pot(x, a : int) -> int:
    mod = x & (2**a - 1)
    return mod

def right_propagate(x: int) -> int:
    return x | (x - 1)

def run_POT():
    for i in range(1000):
        if power_of_two(i):
            print(i)

def run_modPot():
    for i in range(10):
        print(i, i % (2**2) ,mod_pot(i, 2))

def run_rightPropagate():
    for i in range(1000):
        print(i,bin(i), bin(right_propagate(i)))

if __name__ == '__main__':
    # run_POT()
    # print(0<<1)
    # run_modPot()
    run_rightPropagate()