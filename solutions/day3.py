from utils import read_all_lines_from_file


CODE_OF_A_LOWER = ord("a")

CODE_OF_A_UPPER = ord("A")


def convert_ch_to_priority(ch: str) -> int:
    ch_code = ord(ch)
    return (
        ch_code - CODE_OF_A_LOWER + 1
        if ch.islower()
        else ch_code - CODE_OF_A_UPPER + 27
    )


def part1(lines):
    total_sum = 0
    for s in lines:
        middle = len(s) // 2
        left, right = s[:middle], s[middle:]
        general_chs = set(left) & set(right)
        total_sum += sum(map(convert_ch_to_priority, general_chs))
    print(total_sum)


def part2(lines):
    total_sum = 0
    for start in range(0, len(lines), 3):
        general_chs = (
            set(lines[start].strip())
            & set(lines[start + 1].strip())
            & set(lines[start + 2].strip())
        )
        total_sum += sum(map(convert_ch_to_priority, general_chs))
    print(total_sum)


if __name__ == "__main__":
    part1(read_all_lines_from_file("in1.txt"))
