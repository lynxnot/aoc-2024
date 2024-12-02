#!/usr/bin/env python
#


INFILE = "./aoc-d2-input.txt"

############# parse


def parse_input():
    """parse input"""
    reports = []
    with open(INFILE, "r", encoding="utf-8") as f:
        for line in f:
            r = list(map(int, line.strip().split(" ")))
            reports.append(r)

    return reports


############# p1


def is_monotonic_inc(zipped):
    """monotonic up"""
    return all(x < y for x, y in zipped)


def is_monotonic_dec(zipped):
    """monotonic down"""
    return all(x > y for x, y in zipped)


def is_monotonic(zipped):
    """morontonic frobnicator"""
    return is_monotonic_inc(zipped) or is_monotonic_dec(zipped)


def is_kinda_safe(zipped):
    """kinda safe by distance"""
    return all(1 <= abs(x - y) <= 3 for x, y in zipped)


def is_definetely_safe(lst):
    """boringly safe"""
    zipped = list(zip(lst, lst[1:]))
    return is_monotonic(zipped) and is_kinda_safe(zipped)


def solution_p1(reports):
    """solve p1"""
    safe_reports = list(filter(is_definetely_safe, reports))
    return len(safe_reports)


############# p2


def report_dampener(report):
    """ugly dampener bcs f recursion"""
    exploded = [report]
    idx = range(len(report))

    for i in idx:
        dampened = []
        for j in idx:
            if i != j:
                dampened.append(report[j])
        exploded.append(dampened)

    return exploded


def any_safe(report):
    """any safe dumplings out there?"""
    return any(is_definetely_safe(r) for r in report_dampener(report))


def solution_p2(reports):
    """solve p2"""
    safe_dumplings = list(filter(any_safe, reports))
    return len(safe_dumplings)


############# main


def main():
    """main"""

    reports = parse_input()

    # part 1
    print(solution_p1(reports))

    # part 2
    print(solution_p2(reports))


if __name__ == "__main__":
    main()
