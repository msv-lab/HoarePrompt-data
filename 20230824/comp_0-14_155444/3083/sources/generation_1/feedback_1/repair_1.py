def find_playlist(n, songs):
    def dfs(song, playlist):
        nonlocal found
        playlist.append(songs[song][0])

        if len(set(playlist)) == 9:
            found = True
            return playlist

        for next_song in songs[song][2:]:
            if next_song not in playlist:
                result = dfs(next_song, playlist)
                if found:
                    return result

        playlist.pop()
        return []

    playlist = []
    found = False
    for i in range(1, n+1):
        result = dfs(i, [])
        if found:
            return result

    return []


n = int(input())
songs = {}
for i in range(1, n+1):
    artist, t, *after = input().split()
    songs[i] = (artist, int(t), *[int(x) for x in after])

playlist = find_playlist(n, songs)
if playlist:
    print(' '.join(map(str, playlist)))
else:
    print('fail')