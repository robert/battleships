

def render(board_width, board_height, shots):
    header = "+" + "-" * board_width + "+"
    print(header)

    shots_set = set(shots)
    for y in range(board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")

    print(header)

if __name__ == "__main__":
    shots = []

    while True:
        inp = input("Where do you want to shoot?\n")
        # TODO: deal with invalid input
        xstr, ystr = inp.split(",")
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10, 10, shots)

