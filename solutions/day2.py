from utils import read_all_lines_from_file


reason_to_score_opponent = {"A": 1, "B": 2, "C": 3}


reason_to_score_for_me = {"X": 1, "Y": 2, "Z": 3}


DRAW_SCORE = 3
WIN_SCORE = 6


def am_i_win(opponent, me):
    if me == "X":
        return opponent == "C"
    elif me == "Y":
        return opponent == "A"
    else:  # me == 'Z'
        return opponent == "B"


def part1(lines):
    total_score = 0
    for s in lines:
        opponent, me = s.strip().split(" ")
        total_score += reason_to_score_for_me[me]
        if reason_to_score_for_me[me] == reason_to_score_opponent[opponent]:
            total_score += DRAW_SCORE
        elif am_i_win(opponent, me):
            total_score += WIN_SCORE
    print(total_score)


mapping_for_draw = {"A": "X", "B": "Y", "C": "Z"}


mapping_for_lose = {"A": "Z", "B": "X", "C": "Y"}


mapping_for_win = {"A": "Y", "B": "Z", "C": "X"}


def part2(lines):
    total_score = 0
    for s in lines:
        opponent, res = s.strip().split(" ")
        if res == "X":  # need lose
            selected_reason = mapping_for_lose[opponent]
        elif res == "Y":  # need draw
            selected_reason = mapping_for_draw[opponent]
            total_score += DRAW_SCORE
        else:  # need win
            selected_reason = mapping_for_win[opponent]
            total_score += WIN_SCORE
        total_score += reason_to_score_for_me[selected_reason]
    print(total_score)


if __name__ == "__main__":
    part2(read_all_lines_from_file("in.txt"))
