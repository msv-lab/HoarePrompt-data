def song_restart(T, S, q):
    restart_count = 1
    downloaded = S
    while downloaded < T:
        downloaded *= q
        restart_count += 1
    return restart_count

T, S, q = map(int, input().split())
print(song_restart(T, S, q))