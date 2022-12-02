def read_all_lines_from_file(filename="in.txt"):
    with open(filename, "r") as f:
        return f.readlines()
