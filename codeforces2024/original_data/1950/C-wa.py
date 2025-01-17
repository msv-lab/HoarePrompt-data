TIME = {1: "AM", 0: "PM"}


def get_12(h24: str):
    """
    INPUT MUST BE HH:MM
    """
    h, m = map(int, h24.split(":"))
    return f"{h % 12 or 12}:{m:02d} {TIME[h < 12]}"

t = int(input())
while t > 0:
    time = input()
    print(get_12(time))
    t -= 1