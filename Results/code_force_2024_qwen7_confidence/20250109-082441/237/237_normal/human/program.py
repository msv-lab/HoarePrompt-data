n = int(input())
c = input().strip()
p = input().strip()

P_move = {'M': [], 'C': []}  # Professors to move
C_need = {'M': [], 'C': []}  # Classes needing a professor
Swap_buildings = []  # Buildings where we can swap professors

for i in range(n):
    c_i = c[i]
    p_i = p[i]
    building = i + 1  # Buildings are 1-indexed

    if c_i == p_i and c_i != '-':
        continue  # Professor is already at the right place

    if c_i != '-' and p_i != c_i:
        if p_i != '-':
            # Need to swap professors at this building
            Swap_buildings.append((building, p_i, c_i))
        else:
            # Need to bring in a professor
            C_need[c_i].append(building)
    elif c_i == '-' and p_i != '-':
        # Need to move professor away
        P_move[p_i].append(building)
    elif c_i != '-' and p_i == '-':
        # Need to bring in a professor
        C_need[c_i].append(building)

# Now, match professors to classes
plan = []
current_location = None
carrying = None
visited = set()

# Handle swaps first
for building, prof_exp, class_exp in Swap_buildings:
    if carrying is None:
        # Need to pick up a professor to bring here
        if P_move[class_exp]:
            pickup_building = P_move[class_exp].pop()
            if current_location != pickup_building:
                plan.append(f'DRIVE {pickup_building}')
                current_location = pickup_building
            plan.append('PICKUP')
            carrying = class_exp
        else:
            # No professor to bring here, should not happen
            pass
    if current_location != building:
        plan.append(f'DRIVE {building}')
        current_location = building
    plan.append('DROPOFF')
    carrying = None  # Dropped off professor
    plan.append('PICKUP')
    carrying = prof_exp  # Picked up professor to move away
    visited.add(building)

# Now handle remaining professors to move
for exp in ['M', 'C']:
    while P_move[exp]:
        pickup_building = P_move[exp].pop()
        if current_location != pickup_building:
            plan.append(f'DRIVE {pickup_building}')
            current_location = pickup_building
        if carrying is None:
            plan.append('PICKUP')
            carrying = exp
        # Find a class needing this professor
        if C_need[exp]:
            dropoff_building = C_need[exp].pop()
            if current_location != dropoff_building:
                plan.append(f'DRIVE {dropoff_building}')
                current_location = dropoff_building
            plan.append('DROPOFF')
            carrying = None
        else:
            # No class needing this professor, should not happen
            pass

# In case we are still carrying someone, try to drop them off
for exp in ['M', 'C']:
    while C_need[exp]:
        if carrying is None and P_move[exp]:
            # Pick up a professor
            pickup_building = P_move[exp].pop()
            if current_location != pickup_building:
                plan.append(f'DRIVE {pickup_building}')
                current_location = pickup_building
            plan.append('PICKUP')
            carrying = exp
        dropoff_building = C_need[exp].pop()
        if current_location != dropoff_building:
            plan.append(f'DRIVE {dropoff_building}')
            current_location = dropoff_building
        plan.append('DROPOFF')
        carrying = None

print(len(plan))
for cmd in plan:
    print(cmd)