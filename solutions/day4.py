from utils import read_all_lines_from_file


def part1(lines):
    ans = 0
    for s in lines:
        first_pair, second_pair = s.rstrip().split(",")
        first_start, first_end = map(int, first_pair.split("-"))
        second_start, second_end = map(int, second_pair.split("-"))
        if (first_start <= second_start and second_end <= first_end) or (
            second_start <= first_start and first_end <= second_end
        ):
            ans += 1
    print(ans)


def part2(lines):
    ans = 0
    for s in lines:
        first_pair, second_pair = s.rstrip().split(",")
        first_start, first_end = map(int, first_pair.split("-"))
        second_start, second_end = map(int, second_pair.split("-"))
        if (
            (first_start <= second_start and second_end <= first_end)
            or (second_start <= first_start and first_end <= second_end)
            or (first_end >= second_start and first_start <= second_end)
            or (second_end >= first_start and second_start <= first_end)
        ):
            ans += 1
    print(ans)


if __name__ == "__main__":
    part2(read_all_lines_from_file("in1.txt"))
