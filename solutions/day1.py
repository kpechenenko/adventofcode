from utils import read_all_lines_from_file


def regroup_maxs(max1, max2, max3, cur):
    if cur > max1:
        if max1 > max2:
            if max2 > max3:
                max3 = max2
            max2 = max1
        max1 = cur
    elif cur > max2:
        if max2 > max3:
            max3 = max2
        max2 = cur
    elif cur > max3:
        max3 = cur
    return max1, max2, max3


def part2():
    in_lines = read_all_lines_from_file()
    max1: int = 0
    max2: int = 0
    max3: int = 0
    cur: int = 0
    for s in in_lines:
        if s == "" or s == "\n":
            max1, max2, max3 = regroup_maxs(max1, max2, max3, cur)
            cur = 0
        else:
            cur += int(s)
    max1, max2, max3 = regroup_maxs(max1, max2, max3, cur)
    print(max1 + max2 + max3)


if __name__ == "__main__":
    part2()
