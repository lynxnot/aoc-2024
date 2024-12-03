#!/usr/bin/env python
#

import re

INFILE = "./aoc-d3-input.txt"

TESTS = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

############# parse


def parse_input():
    """parse input"""
    mangled = ""
    with open(INFILE, "r", encoding="utf-8") as f:
        for line in f:
            if not (line is None or line == ""):
                mangled += line.strip()

    return mangled


############# p1


def demangler(mangled):
    """regex deblobinator"""
    valid = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return re.findall(valid, mangled)


def mul_sum(matches):
    """p2 enjoyer will be"""
    return sum(int(x) * int(y) for x, y in matches)


def solution_p1(mangled):
    """solve p1"""
    matches = demangler(mangled)
    return mul_sum(matches)


############# p2


def preprocess(mangled):
    """the ungreedy does that dont"""
    pregex = re.compile(r"don't\(\).*?do\(\)")
    return re.sub(pregex, "@@@@@@@@@@@@@@@@", mangled)


def solution_p2(mangled):
    """solve p2"""
    return mul_sum(demangler(preprocess(mangled)))


############# main


def main():
    """main"""

    mangled = parse_input()

    # part 1
    print(solution_p1(mangled))

    # part 2
    print(solution_p2(mangled))


if __name__ == "__main__":
    main()
