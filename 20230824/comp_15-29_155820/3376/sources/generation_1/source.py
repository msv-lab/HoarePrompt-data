def optimal_xp(f, families, n, caught):
    xp = 0
    max_xp = 0
    max_xp_time = 0
    egg_active = False
    
    for family in families:
        max_xp += family[1] * 100
        xp += family[1] * 3
        
        for i in range(2, len(family), 2):
            candy = family[i + 1]
            xp_cost = family[i]
            
            if egg_active:
                xp += xp_cost * 2
                
            max_xp += xp_cost * 500
        
        if max_xp > max_xp_time:
            max_xp_time = max_xp
    
    for i in range(n):
        time = caught[i][0]
        pokemon = caught[i][1]
        
        if pokemon == "BlessedEgg":
            egg_active = True
        
        if time >= max_xp_time and pokemon != "BlessedEgg":
            break
    
    return xp

f = int(input())
families = []

for _ in range(f):
    family = input().split()
    family_size = int(family[0])
    candies = []
    for i in range(1, len(family) - 1, 2):
        candies.append(int(family[i + 1]))
    
    families.append(candies)

n = int(input())
caught = []

for _ in range(n):
    catch = input().split()
    time = int(catch[0])
    pokemon = catch[1]
    caught.append((time, pokemon))

print(optimal_xp(f, families, n, caught))