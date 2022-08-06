first = input("ENTER FIRST PLAYERS NAME --> ")
second = input("ENTER SECOND PLAYERS NAME --> ")
players = [first, second]

a = " 1 | 2 | 3 \n"\
    " 4 | 5 | 6 \n"\
    " 7 | 8 | 9 \n"

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_list = []
second_list = []
answers = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [7, 8, 9], [3, 6, 9], [7, 5, 3]]

resume = True
while resume:
    winner = 0
    for i in players:
        if winner == 1:
            break
        if players.index(i) == 0:
            sign = "X"
            print(a)
            b = input(f"{i}, select your move --> ")
            if int(b) in my_list:
                a = a.replace(b, f"{sign}")
                my_list.remove(int(b))
                first_list.append(int(b))
                for k in answers:
                    if set(k).issubset(set(first_list)):
                        print(a)
                        print(f"Congratulations {players[0]}!")
                        ask = input("Do you want to play again? Type Y or N.").lower()
                        if ask == "y":
                            a = " 1 | 2 | 3 \n" \
                                " 4 | 5 | 6 \n" \
                                " 7 | 8 | 9 \n"

                            my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            first_list = []
                            second_list = []
                            winner = 1
                        else:
                            resume = False
                            winner = 1
            else:
                u_turn = True
                while u_turn:
                    print("INVALID INPUT!!!")
                    print(a)
                    b = input(f"{i}, select your move again --> ")
                    if int(b) in my_list:
                        a = a.replace(b, f"{sign}")
                        my_list.remove(int(b))
                        first_list.append(int(b))
                        for m in answers:
                            if set(m).issubset(set(first_list)):
                                print(a)
                                print(f"Congratulations {players[0]}!")
                                ask = input("Do you want to play again? Type Y or N.").lower()
                                if ask == "y":
                                    a = " 1 | 2 | 3 \n" \
                                        " 4 | 5 | 6 \n" \
                                        " 7 | 8 | 9 \n"

                                    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    first_list = []
                                    second_list = []
                                    winner = 1
                                else:
                                    resume = False
                                    winner = 1
                        u_turn = False
        else:
            sign = "0"
            print(a)
            b = input(f"{i}, select your move --> ")
            if int(b) in my_list:
                a = a.replace(b, f"{sign}")
                my_list.remove(int(b))
                second_list.append(int(b))
                for l in answers:
                    if set(l).issubset(set(second_list)):
                        print(a)
                        print(f"Congratulations, {players[1]}!")
                        ask = input("Do you want to play again? Type Y or N.").lower()
                        if ask == "y":
                            a = " 1 | 2 | 3 \n" \
                                " 4 | 5 | 6 \n" \
                                " 7 | 8 | 9 \n"

                            my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                            first_list = []
                            second_list = []
                            winner = 1
                        else:
                            resume = False
                            winner = 1
            else:
                v_turn = True
                while v_turn:
                    print("INVALID INPUT!!!")
                    print(a)
                    b = input(f"{i}, select your move again --> ")
                    if int(b) in my_list:
                        a = a.replace(b, f"{sign}")
                        my_list.remove(int(b))
                        first_list.append(int(b))
                        for d in answers:
                            if set(d).issubset(set(second_list)):
                                print(a)
                                print(f"Congratulations {players[0]}!")
                                ask = input("Do you want to play again? Type Y or N.").lower()
                                if ask == "y":
                                    a = " 1 | 2 | 3 \n" \
                                        " 4 | 5 | 6 \n" \
                                        " 7 | 8 | 9 \n"

                                    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    first_list = []
                                    second_list = []
                                    winner = 1
                                else:
                                    resume = False
                                    winner = 1
                        v_turn = False







