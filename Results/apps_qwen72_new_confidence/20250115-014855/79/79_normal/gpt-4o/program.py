MOD = 10**9 + 7

def count_playlists(songs, n, T):
    def backtrack(current_time, last_genre, used_songs):
        if current_time == T:
            return 1
        if current_time > T:
            return 0
        
        count = 0
        for i in range(n):
            t_i, g_i = songs[i]
            if i not in used_songs and g_i != last_genre:
                used_songs.add(i)
                count = (count + backtrack(current_time + t_i, g_i, used_songs)) % MOD
                used_songs.remove(i)
        
        return count
    
    return backtrack(0, -1, set())

# Reading input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
T = int(data[1])

songs = []
for i in range(n):
    t_i = int(data[2 + 2 * i])
    g_i = int(data[3 + 2 * i])
    songs.append((t_i, g_i))

# Calculate the number of valid playlists
result = count_playlists(songs, n, T)
print(result)
