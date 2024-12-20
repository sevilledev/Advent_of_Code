import contextlib

top, bottom = open("puzzle.txt").read().split("\n\n")

rules = set()
for line in top.splitlines():
    a, b = line.split("|")
    rules.add((int(a), int(b)))

order_list = [list(map(int, line.split(","))) for line in bottom.splitlines()]

res = 0


def check(order):
    for rule in rules:
        first, second = rule
        with contextlib.suppress(ValueError):
            f_index = order.index(first)
            s_index = order.index(second)
            if f_index > s_index:
                return False
    return True


for order in order_list:
    mid = (len(order) - 1) // 2
    if check(order):
        res += order[mid]


print(res)