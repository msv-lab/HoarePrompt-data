def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        healths = list(map(int, input().split()))
        positions = list(map(int, input().split()))
 
        # Sort the monsters by their distance from point 0.
        monsters = sorted(zip(positions, healths), key=lambda x: abs(x[0]))
        
        # Can we kill all monsters before any of them reaches 0?
        total_bullets_used = 0
        success = True
        for i in range(n):
            position, health = monsters[i]
            distance = abs(position)
            # Calculate the number of seconds available before the monster reaches 0.
            time_available = distance
            # Calculate the number of bullets needed for this monster.
            bullets_needed = health
 
            # If the total bullets we have used + the bullets needed for this monster exceed the time available, we lose.
            if total_bullets_used + bullets_needed > time_available:
                success = False
                break
            # Otherwise, add the bullets used for this monster.
            total_bullets_used += bullets_needed
        
        print("YES" if success else "NO")
 
if __name__ == "__main__":
    solve()