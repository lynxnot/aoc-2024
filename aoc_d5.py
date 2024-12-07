#!/usr/bin/env python
#

from functools import partial

# INFILE = "./aoc_d5-input.t.txt"
INFILE = "./aoc_d5-input.txt"


############# parse


def parse_input() -> tuple[dict, list]:
    """parse input"""
    rules = {}
    updates = []
    in_rules = True
    with open(INFILE, "r", encoding="utf-8") as f:
        for line in f:
            sl = line.strip()
            if sl == "":
                in_rules = False
                continue

            if in_rules:
                a, b = map(int, sl.split("|"))
                if a in rules:
                    rules[a].append(b)
                else:
                    rules[a] = [b]

            else:
                updates.append(list(map(int, sl.split(","))))

    return rules, updates


############# p1


def check_order(rules: dict, update: list) -> bool:
    """check_order"""

    for i in range(1, len(update)):
        el = update[i]
        before = update[:i]
        if el in rules:
            if any(x in rules[el] for x in before):
                return False

    return True


def solution_p1(rules: dict, updates: list) -> int:
    """solve p1"""

    partial_check = partial(check_order, rules)
    valid_updates = list(filter(partial_check, updates))

    return sum(map(lambda lst: lst[len(lst) // 2], valid_updates))


############# p2


def fix_order(rules: dict, updt: list):
    """fix list order"""
    for i in range(len(updt) - 1):
        cur = updt[i]
        nxt = updt[i + 1]
        if nxt in rules and cur in rules[nxt]:
            nupdt = updt[:i] + [nxt, cur] + updt[i + 2 :]
            return fix_order(rules, nupdt)

    return updt


def solution_p2(rules: dict, updates: list):
    """solve p2"""
    partial_check = partial(check_order, rules)
    borked_updates = list(filter(lambda lst: not partial_check(lst), updates))

    partial_fixer = partial(fix_order, rules)
    fixed_updates = list(map(partial_fixer, borked_updates))

    return sum(map(lambda lst: lst[len(lst) // 2], fixed_updates))


############# main


def main():
    """main"""

    rules, updates = parse_input()

    # part 1
    print(solution_p1(rules, updates))

    # part 2
    print(solution_p2(rules, updates))


if __name__ == "__main__":
    main()
