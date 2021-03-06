def play_sound(play_sound):
    import pyglet
    song = pyglet.media.load('Casio-MT-45-16-Beat.wav')
    song.play()
    return play_sound


def play_winsound(play_winsound):
    import pyglet
    song = pyglet.media.load('1_person_cheering-Jett_Rifkin-1851518140.wav')
    song.play()
    return play_sound


def sep(sep):
    import sys
    sep = input("Select game style: Traditional (1) Seppuku(2): ")
    if sep == "q":
        print("GOOD BYE!")
        sys.exit(0)
    while sep != "1" and sep != "2":
        print("Game style have to set 1 or 2")
        sep = input(":")
        continue
    else:
        sep = int(sep)
        return sep


def difficulty(difficulty):
    import sys
    difficulty = input("Select difficulty level: Amateur (1) Godlike(2): ")
    if difficulty == "q":
        print("GOOD BYE!")
        sys.exit(0)
    while difficulty != "1" and difficulty != "2":
        print("Difficulty have to set 1 or 2")
        difficulty = input(":")
        continue
    else:
        difficulty = int(difficulty)
        return difficulty


def mode(mode):
    import sys
    mode = input("Please select a game mode: ")
    if mode == "q":
        print("GOOD BYE!")
        sys.exit(0)
    while mode != "1" and mode != "2" and mode != "3":
        print("mode must be 1,2, or 3")
        mode = input(": ")
        continue
    else:
        return mode


def print_text3():
    print("Modes: Human vs. Human (1) - Human vs. Computer (2) - Computer vs. Human (3)")


def checkLine(char, board):
    if board[1] == char and board[2] == char and board[3] == char:
        return True
    if board[4] == char and board[5] == char and board[6] == char:
        return True
    if board[7] == char and board[8] == char and board[9] == char:
        return True
    if board[1] == char and board[5] == char and board[9] == char:
        return True
    if board[3] == char and board[5] == char and board[7] == char:
        return True
    if board[1] == char and board[4] == char and board[7] == char:
        return True
    if board[2] == char and board[5] == char and board[8] == char:
        return True
    if board[3] == char and board[6] == char and board[9] == char:
        return True


def show(board):
    print(board[7], '|', board[8], '|', board[9])
    print("---------")
    print(board[4], '|', board[5], '|', board[6])
    print("---------")
    print(board[1], '|', board[2], '|', board[3])


def restartgame(step1, board, board1):
    show(board1)
    return board == [" "] * 10
    return step1 == 0


def comprandom(signal, step1, board):
    import random
    if signal == "X" and step1 == 0:
        slots = (1, 3, 5, 7, 9)
        return random.choice(slots)

    if signal == "X" and step1 == 1:
        if (board[1] == "X" or board[9] == "X") and (board[7] == " "):
            return 7
        if (board[1] == "X" or board[9] == "X") and (board[3] == " "):
            return 3
        if (board[3] == "X" or board[7] == "X") and (board[1] == " "):
            return 1
        if (board[3] == "X" or board[7] == "X") and (board[9] == " "):
            return 9
        if board[5] == "X":
            blist = []
            for i in range(1, 10, 2):
                if board[i] == " ":
                    blist.append(i)
            return random.choice(blist)

    if signal == "X" and step1 > 1:
        emptylist = []
        for i in range(1, 10):
            if board[i] == " ":
                emptylist.append(i)

        for i in emptylist:

            board[i] = "X"
            if checkLine('X', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "O"
            if checkLine('O', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        return random.choice(emptylist)

    if signal == "O" and step1 == 1:
        if board[5] == " ":
            return 5
        for i in range(1, 10):
            if board[i] == "X":
                memi = i
        slots = []
        for i in range(1, 10, 2):
            if i != memi:
                slots.append(i)
        return random.choice(slots)

    if signal == "O" and step1 > 1:
        emptylist = []
        for i in range(1, 10):
            if board[i] == " ":
                emptylist.append(i)

        for i in emptylist:

            board[i] = "O"
            if checkLine('O', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        for i in emptylist:

            board[i] = "X"
            if checkLine('X', board):
                board[i] = " "
                return i
            else:
                board[i] = " "

        return random.choice(emptylist)


def compbasic(signal, step1, board):
    import random
    if signal == "X" and step1 == 0:
        slots = (1, 3, 5, 7, 9)
        return random.choice(slots)

    if signal == "X" and step1 == 1:
        if (board[1] == "X" or board[9] == "X") and (board[7] == " "):
            return 7
        if (board[1] == "X" or board[9] == "X") and (board[3] == " "):
            return 3
        if (board[3] == "X" or board[7] == "X") and (board[1] == " "):
            return 1
        if (board[3] == "X" or board[7] == "X") and (board[9] == " "):
            return 9
        if board[5] == "X":
            blist = []
            for i in range(1, 10, 2):
                if board[i] == " ":
                    blist.append(i)
            return random.choice(blist)

    if signal == "X" and step1 > 1:
        for i in range(1, 10):
            if board[i] == (" "):
                return i

    if signal == "O" and step1 > 0:
        for i in range(1, 10):
            if board[i] == (" "):
                return i
