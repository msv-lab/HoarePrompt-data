def circle_dance(N, moves):
    positions = [''] * N
    for i in range(N):
        if moves[i] == 0:
            positions[i] = 'L'
        elif moves[i] == N - 1:
            positions[i] = 'R'
        elif moves[i] % 2 == 0:
            positions[i] = 'R'
        else:
            positions[i] = 'L'
    return "".join(positions)