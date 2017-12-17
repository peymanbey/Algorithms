# -*- coding: utf-8 -*-
"""
peymanbey@github

Hackerrank Snake Ladder game
"""
import numpy as np

def read_games():
    """
    Read theh games from .txt file
    """
    game_list = []
    die_prob_list = []
    with open("sampleInput.txt") as f:
        N = int(f.readline())
        for _ in range(N):
            die_prob_list.append(list(map(float, f.readline().split(","))))
            _, _ = map(int, f.readline().split(","))
            ladders = [list(map(int, pair.split(","))) for pair in f.readline().split()]
            snakes = [list(map(int, pair.split(","))) for pair in f.readline().split()]
            game_list.append(dict(snakes + ladders))

    return die_prob_list, game_list


def play_a_move(game, die_val, current):
    return current + game.get(die_val, die_val)

def toss_die(dieProbability):
    return np.random.choice(len(dieProbability), 1,
                            p=dieProbability, replace=True)


def play_a_game(game, dieProbability):
    current = 1
    n = 0
    while current != 100:
        n += 1
        dieVal = toss_die(dieProbability)
        temp = play_a_move(game, dieVal[0]+1, current)
        if  temp <= 100:
            current = temp
    return n

def mov_average(a, m_before, n):
    return m_before + (a - m_before) / n
#####
if __name__ == "__main__":
    dieProbs, games = read_games()

    expectedList = ""
    for dieProb, board in zip(dieProbs, games):
        expected = 0
        for step in range(5000):
            sample = play_a_game(board, dieProb)
            expected = mov_average(sample, expected, step+1)
        expectedList = "\n".join([expectedList, str(expected)])

    print(expectedList)
