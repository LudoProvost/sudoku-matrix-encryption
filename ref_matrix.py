import numpy as np


def get_matrix(x_0, r, M):
    return rescale_ref_matrix(transpose(get_sudoku_matrix(M, get_secret_sequence(get_chaotic_sequence(x_0, r, M ** 2))), M), M)


def get_chaotic_sequence(x_0, r, N):
    chaotic_sequence = np.empty(N, dtype=object)
    chaotic_sequence[0] = (x_0, 1)

    for x in range(1, N):
        chaotic_sequence[x] = (r * chaotic_sequence[x - 1][0] * (1 - chaotic_sequence[x - 1][0]), x + 1)

    return chaotic_sequence


def get_secret_sequence(chaotic_sequence):
    N = len(chaotic_sequence)

    for i in range(N):
        for j in range(0, N - i - 1):
            if chaotic_sequence[j][0] > chaotic_sequence[j + 1][0]:
                temp = chaotic_sequence[j]
                chaotic_sequence[j] = chaotic_sequence[j + 1]
                chaotic_sequence[j + 1] = temp

    secret_sequence = np.empty(N)

    for x in range(N):
        secret_sequence[x] = chaotic_sequence[x][1]

    return secret_sequence


def generate_latin_square(number_sequence):
    M = len(number_sequence)
    latin_square = np.empty((M, M), dtype=object)
    latin_square[0] = number_sequence
    for row in range(1, M):
        latin_square[row] = ring_shift((latin_square[row - 1]))

    return latin_square.ravel()


def ring_shift(number_sequence):
    M = len(number_sequence)

    new_sequence = np.empty(M, dtype=object)
    new_sequence[0:M - 1] = (number_sequence[1:M]).astype(object)
    new_sequence[M - 1] = number_sequence[0]
    return new_sequence


def get_sudoku_matrix(M, secret_sequence):
    L_seed = np.empty(M, dtype=object)
    for i in range(0, M):
        L_seed[i] = generate_latin_square(secret_sequence[(M * i):((M * i) + M)])

    return (generate_latin_square(L_seed)).T


def transpose(L, M):
    L_rearranged = np.zeros((M ** 2, M ** 2))

    # TESTED DIFFERENT ALGORITHMS

    # for i in range(M**2):
    #     for j in range(M**2):
    #         result[i][j] = L[(j//3 + i)%9][(j%3*3 + i)%9]
    #
    # for i in range(3):
    #     for j in range(3):
    #         for k in range(3):
    #             for l in range(3):
    #                 result[i * 3 + k][j * 3 + l] = L[i * 3 + l][j * 3 + k]

    for sub_array in range(M ** 2):
        sub_array_col = sub_array % M
        sub_array_row = sub_array // M
        for i in range(M ** 2):
            i_col = i % M
            i_row = i // M
            L_rearranged[(M * sub_array_col) + i_col][(M * sub_array_row) + i_row] = L[sub_array][i]

    S = np.zeros((M ** 2, M ** 2))
    for i in range(M ** 2):
        S[i] = L_rearranged[M * (i % M) + i // M]

    return S


def rescale_ref_matrix(S, M):
    # substract 1 to sudoku ref matrix
    S_sub = S - 1

    # rescale for color values
    S_rescaled = S_sub * (255 / ((M ** 2) + 1))

    return S_rescaled