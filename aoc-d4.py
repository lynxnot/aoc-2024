#!/usr/bin/env python
#


INFILE = "./aoc-d4-input.txt"


############# parse


def parse_input():
    """parse input"""
    rows = []
    with open(INFILE, "r", encoding="utf-8") as f:
        for line in f:
            if not (line is None or line == ""):
                ln = list(line.strip())
                rows.append(ln)

    return rows


############# p1


def check_xmas(rows, r, c):
    """check at position"""
    size = len(rows)
    lt = 3
    ht = size - 4
    count = 0

    # check l-to-r
    if (
        c <= ht
        and rows[r][c] == "X"
        and rows[r][c + 1] == "M"
        and rows[r][c + 2] == "A"
        and rows[r][c + 3] == "S"
    ):
        count += 1

    # check r-to-l
    if (
        c >= lt
        and rows[r][c] == "X"
        and rows[r][c - 1] == "M"
        and rows[r][c - 2] == "A"
        and rows[r][c - 3] == "S"
    ):
        count += 1

    # check t-to-b
    if (
        r <= ht
        and rows[r][c] == "X"
        and rows[r + 1][c] == "M"
        and rows[r + 2][c] == "A"
        and rows[r + 3][c] == "S"
    ):
        count += 1

    # check b-to-t
    if (
        r >= lt
        and rows[r][c] == "X"
        and rows[r - 1][c] == "M"
        and rows[r - 2][c] == "A"
        and rows[r - 3][c] == "S"
    ):
        count += 1

    # check d-up-r
    if (
        r >= lt
        and c <= (size - 4)
        and rows[r][c] == "X"
        and rows[r - 1][c + 1] == "M"
        and rows[r - 2][c + 2] == "A"
        and rows[r - 3][c + 3] == "S"
    ):
        count += 1

    # check d-up-l
    if (
        r >= lt
        and c >= lt
        and rows[r][c] == "X"
        and rows[r - 1][c - 1] == "M"
        and rows[r - 2][c - 2] == "A"
        and rows[r - 3][c - 3] == "S"
    ):
        count += 1

    # check d-down-r
    if (
        r <= ht
        and c <= ht
        and rows[r][c] == "X"
        and rows[r + 1][c + 1] == "M"
        and rows[r + 2][c + 2] == "A"
        and rows[r + 3][c + 3] == "S"
    ):
        count += 1

    # check d-down-l
    if (
        r <= ht
        and c >= lt
        and rows[r][c] == "X"
        and rows[r + 1][c - 1] == "M"
        and rows[r + 2][c - 2] == "A"
        and rows[r + 3][c - 3] == "S"
    ):
        count += 1

    return count


def solution_p1(rows):
    """solve p1"""
    size = len(rows)
    cnt = 0
    for r in range(size):
        for c in range(size):
            # print((r, c))
            cnt += check_xmas(rows, r, c)

    return cnt


############# p2


def check_x_mas(rows, r, c):
    """check x mas"""

    if rows[r][c] != "A":
        return 0

    # check MAS - MAS
    if (
        rows[r - 1][c - 1] == "M"
        and rows[r + 1][c + 1] == "S"
        and rows[r + 1][c - 1] == "M"
        and rows[r - 1][c + 1] == "S"
    ):
        return 1

    # check SAM - MAS
    if (
        rows[r - 1][c - 1] == "S"
        and rows[r + 1][c + 1] == "M"
        and rows[r + 1][c - 1] == "M"
        and rows[r - 1][c + 1] == "S"
    ):
        return 1

    # check SAM - SAM
    if (
        rows[r - 1][c - 1] == "S"
        and rows[r + 1][c + 1] == "M"
        and rows[r + 1][c - 1] == "S"
        and rows[r - 1][c + 1] == "M"
    ):
        return 1

    # check MAS - SAM
    if (
        rows[r - 1][c - 1] == "M"
        and rows[r + 1][c + 1] == "S"
        and rows[r + 1][c - 1] == "S"
        and rows[r - 1][c + 1] == "M"
    ):
        return 1

    return 0


def solution_p2(rows):
    """solve p2"""
    size = len(rows) - 1
    count = 0
    for i in range(1, size):
        for j in range(1, size):
            count += check_x_mas(rows, i, j)

    return count


############# main


def main():
    """main"""

    rows = parse_input()

    # part 1
    print(solution_p1(rows))

    # part 2
    print(solution_p2(rows))


if __name__ == "__main__":
    main()
