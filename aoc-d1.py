#!/usr/bin/env python
#

from functools import partial

INFILE = "./aoc-d1-input.txt"


def distance(t):
    """distance"""
    return abs(t[0] - t[1])


def equals(i, j):
    """equals"""
    return i == j


def parse_input():
    """parse input"""
    left = []
    right = []

    with open(INFILE, "r", encoding="utf-8") as f:
        for line in f:
            a, b = line.strip().split("   ")
            left.append(int(a))
            right.append(int(b))

    return left, right


def solution_p1(left, right):
    """solution part 1"""
    sorted_l = sorted(left)
    sorted_r = sorted(right)

    return sum(map(distance, zip(sorted_l, sorted_r)))


def solution_p2(left, right):
    """part 2"""
    cache = {}

    for n in left:
        if n in cache:
            continue

        predicate = partial(equals, n)
        c = len(list(filter(predicate, right)))
        cache[n] = c

    similarity_score = 0
    for k, v in cache.items():
        similarity_score += k * v

    return similarity_score


def main():
    """main"""

    left, right = parse_input()

    # part 1
    print(solution_p1(left, right))

    # part 2
    print(solution_p2(left, right))


if __name__ == "__main__":
    main()
