if __name__ == '__main__':
    marksheet = []
    scoresheet = []
    for _ in range(int(input())):  # input leke direct into the range
        name = input()
        score = float(input())
        marksheet += [[name, score]]  # list will contain the name and score, DONT FORGOT TO PUT LIST [].
        scoresheet += [score]         # + is added to add the name and score adjacent in the list.

    x = sorted(set(scoresheet))[1]  # It'll sort the score into ascending order and then the 2nd score will
                                    # be the required score.

    for n, s in sorted(marksheet):          # name,score hogya ye n,s
        if s == x:                          # second score and score match hogya toh it'll print the name.
            print(n)