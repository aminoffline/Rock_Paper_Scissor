import random as rnd

def RSP(times_to_playe=1):
    rsp = ["Rock", "Scissor", "Paper"]
    p_wins = c_wins = 0
    print("Hi Welocome to Rock Scissor Paper game \n Please choose one ")
    for times in range(times_to_playe):
        player = input("Enter Your Pick :").lower().capitalize()
        if player not in rsp:
            print("u Fucked it up , try again")
            break
        computer = rnd.choice(rsp)
        for i in rsp:
            if player == i and computer == i:
                print("this round is Tie")
                break

        if player == "Paper":
            if computer == "Rock":
                print("U Win This Round")
                p_wins += 1

            elif computer == "Scissor":
                print("U lost This Round")
                c_wins += 1

        elif player == "Rock":
            if computer == "Paper":
                print("U lost This Round")
                c_wins += 1

            elif computer == "Scissor":
                print("U win This Round")
                p_wins += 1

        elif player == "Scissor":
            if computer == "Rock This Round":
                print("U lost")
                c_wins += 1

            elif computer == "Paper":
                print("U Win This Round")
                p_wins += 1

    if p_wins > c_wins:
        print(f"U win {p_wins} to {c_wins} ")
    elif p_wins < c_wins:
        print(f"U lost {c_wins} to {p_wins} \n Loooooooser")
    elif p_wins == c_wins:
        print("Its Tie")
RSP(times_to_playe=int(input("How many times U wanna Playe: ")))