def convert(s: str, numRows: int) -> str:
    rows = ["" for i in range(numRows)]
    rowNum = 0
    inc = -1
    for ch in s:
        print(rowNum, end="", sep=" ")
        rows[rowNum] += ch
        if rowNum + 1 ==  numRows or rowNum == 0:
            inc = inc * -1
       
        rowNum += inc
        rowNum = min(numRows - 1, rowNum)
        rowNum = max(0, rowNum)

    return "".join(rows)


if __name__ == '__main__':
    print(convert("PAYPALISHIRING", 4))
    print(convert("PAYPALISHIRING", 3))

    print(convert("AB", 1))