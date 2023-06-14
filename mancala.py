import time
fieldsA = [4, 4, 4, 4, 4, 4]
fieldsB = [4, 4, 4, 4, 4, 4]
scoreA = 0
scoreB = 0
balls = 0
finished = False
counter = 0
player = "A"
wait_time = .5


def showField():
    print("#####################################")
    print("stones left: " + str(balls))
    print("score A: " + str(scoreA))
    print(fieldsA)
    print(fieldsB)
    print("score B: " + str(scoreB))
    print("#####################################\n")


def start(x):
    if player == "A":
        if fieldsA[x] > 0:
            play(0, x)
            return True
        else:
            return False
    else:
        if fieldsB[x] > 0:
            play(1, x)
            return True
        else:
            return False


def play(p, x):
    global balls
    balls = 0
    if p == 0:
        if fieldsA[x] > 0:
            balls = fieldsA[x]
            fieldsA[x] = 0
            walk(p, x+1)
    else:
        if fieldsB[x] > 0:
            balls = fieldsB[x]
            fieldsB[x] = 0
            walk(p, x+1)


def walk(p, x):
    global scoreA
    global scoreB
    global balls
    while balls > 0:
        showField()
        time.sleep(wait_time)
        print("p", p, "x", x)
        if x < 7:
            if x == 6:
                if p == 0 and player == "A":
                    scoreA += 1
                    p = 1
                    x = 0
                    if balls == 1:
                        started = False
                        while not started:
                            x_in = input("next move:\n")
                            if int(x_in) > 0 and int(x_in) < 7:
                                if start(int(x_in)-1):
                                    started = True
                                else:
                                    print("invalid input!")
                elif p == 1 and player == "B":
                    scoreB += 1
                    p = 0
                    x = 0
                    if balls == 1:
                        started = False
                        while not started:
                            x_in = input("next move:\n")
                            if int(x_in) > 0 and int(x_in) < 7:
                                if start(int(x_in)-1):
                                    started = True
                                else:
                                    print("invalid input!")
                elif p == 0:
                    p = 1
                    x = 0
                else:
                    p = 0
                    x = 0

            else:
                if p == 0:
                    fieldsA[x] += 1
                else:
                    fieldsB[x] += 1
                x += 1
            balls -= 1
            if balls == 0:
                if p == 0:
                    #fieldsA[x-1] += 1
                    if fieldsA[x-1] > 1:
                        play(p, x-1)
                else:
                    #fieldsB[x-1] += 1
                    if fieldsB[x-1] > 1:
                        play(p, x-1)


while not finished:
    showField()
    if counter % 2 == 0:
        player = "A"
    else:
        player = "B"
    x = input("move player " + player+"\n")
    if int(x) > 0 and int(x) < 7:
        if start(int(x)-1):
            counter += 1
        else:
            print("invalid input!")
    else:
        print("invalid input!")
