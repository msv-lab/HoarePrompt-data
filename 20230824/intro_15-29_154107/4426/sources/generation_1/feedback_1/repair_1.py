days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
S = input()

if S not in days:
    print("Invalid day")
    exit()

next_Sunday = (days.index('SUN') - days.index(S)) % 7

if next_Sunday == 0:
    next_Sunday = 7

print(next_Sunday)