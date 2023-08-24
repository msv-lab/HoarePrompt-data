x = int(input())
hh, mm = map(int, input().split())

button_presses = 0

while True:
    if '7' in str(hh) or '7' in str(mm):
        break
    mm -= x
    if mm < 0:
        mm += 60
        hh -= 1
    if hh < 0:
        hh += 24
    button_presses += 1

print(button_presses)