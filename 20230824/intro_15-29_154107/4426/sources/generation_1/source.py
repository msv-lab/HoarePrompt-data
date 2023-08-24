days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
S = input()
next_Sunday = (days.index('SUN') - days.index(S)) % 7
print(next_Sunday)