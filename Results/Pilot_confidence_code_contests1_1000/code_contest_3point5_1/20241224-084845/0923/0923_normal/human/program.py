n = input()
field = raw_input()
power = map(int, raw_input().split())

pos = 0
while 0 <= pos < n and power[pos] != 0:
    power[pos], pos = 0, pos + (2 * (field[pos] == '>') - 1) * power[pos]

print ("INFINITE" if 0 <= pos < n else "FINITE")
