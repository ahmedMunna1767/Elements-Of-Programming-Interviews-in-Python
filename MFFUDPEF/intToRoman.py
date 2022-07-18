def intToRoman(num: int) -> str:
    values = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }

    out_str = ""
    while num:
        if num >= 900:
            if num >= 1000:
                out_str += values[1000]
                num = num - 1000
            else:
                out_str += values[900]
                num = num - 900

            continue

        if num >= 400:
            if num >= 500:
                out_str += values[500]
                num = num - 500
            else:
                out_str += values[400]
                num = num - 400
            
            continue

        if num >= 90:
            if num >= 100:
                out_str += values[100]
                num = num - 100
            else:
                out_str += values[90]
                num = num - 90
            
            continue

        if num >= 40:
            if num >= 50:
                out_str += values[50]
                num = num - 50
            else:
                out_str += values[40]
                num = num - 40
            
            continue

        if num >= 9:
            if num >= 10:
                out_str += values[10]
                num = num - 10
            else:
                out_str += values[9]
                num = num - 9
            
            continue

        if num >= 4:
            if num >= 5:
                out_str += values[5]
                num = num - 5
            else:
                out_str += values[4]
                num = num - 4
            
            continue

        out_str += values[1]
        num = num - 1
    return out_str


if __name__ == '__main__':
    for i in range(500):
        print(intToRoman(i))





