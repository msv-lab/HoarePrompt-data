def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        
        # Combine the health and position into tuples, and sort by distance from 0.
        monsters = sorted(zip(x, a), key=lambda p: abs(p[0]))
        
        bullets_used = 0
        can_survive = True
        
        for pos, health in monsters:
            distance = abs(pos)
            # Total bullets needed by now
            total_bullets_needed = bullets_used + health
            
            # If the total bullets needed exceed the time available, we can't survive
            if total_bullets_needed > distance * k:
                can_survive = False
                break
            
            # Update the number of bullets used
            bullets_used += health
        
        print("YES" if can_survive else "NO")
 
if __name__ == "__main__":
    solve()