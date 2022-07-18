# Maintain Order

from numpy import equal


def dutch_flag_partition_maintain_order(arr: list, pivot: int) -> list:
    more = []
    equal = []
    less = []

    for i in arr:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            less.append(i)
        else:
            more.append(i)

    return less + equal + more


def dutch_flag_partition(arr: list, pivot: int) -> list:
    #pivot = arr[pivotIndex]
    smaller, equal, larger = 0, 0, len(arr)
    while equal < larger:
        if arr[equal] < pivot:
            if smaller != equal:
                arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller = smaller + 1
            equal = equal + 1
        elif arr[equal] == pivot:
            equal = equal + 1
        else:
            larger = larger - 1
            arr[larger], arr[equal] = arr[equal], arr[larger]

    largeSet = arr[larger:]
    largeSet = largeSet[:: -1]
    smallSet = arr[:equal]
    return smallSet + largeSet

def even_odd_partition(arr: list) -> list:
    even, odd = 0, len(arr)

    while even < odd:
        if arr[even] % 2 == 0:
            even = even + 1
        else:
            odd = odd - 1
            arr[even], arr[odd] = arr[odd], arr[even]

    return arr

# Variant 4 types of keys
def same_key_togather(arr):
    RED, GREEN, YELLOW, VIOLET = range(4)

    key_1, key_2 , key_3, key_4 = 0, 0, 0, 0
    print(GREEN)
    return(arr)

def test_partition():
    arr = [-3, 0, -1, 1, 1, -5, 3, 0, 4, 2]
    allEven = [2, 2,2, 4]
    allOdd = [3, 1, 5, -2]
    print(dutch_flag_partition(arr=arr, pivot= -5))
    print(even_odd_partition(arr= arr))
    print(even_odd_partition(arr=allEven))
    print(even_odd_partition(arr=allOdd))


if __name__ == '__main__':
    arr = [9,12,5,10,14,3,10]

    print(dutch_flag_partition_maintain_order(arr, 10))
    # test_partition()
    """ arr = [0,1,2,3, 0,1,2,3, 0,1,2,3]
    print(same_key_togather(arr=arr)) """

