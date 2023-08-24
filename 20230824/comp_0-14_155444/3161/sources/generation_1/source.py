from typing import List

def count_differences(picture: List[List[int]]) -> int:
    n = len(picture)
    count = 0
    for i in range(n):
        for j in range(n):
            if picture[i][j] != picture[0][0]:
                count += 1
    return count

def paint_picture(n: int, target: List[str]) -> List[str]:
    picture = [['0'] * n for _ in range(n)]
    return picture

n = int(input())
target = [input() for _ in range(n)]

print(count_differences(target))
for row in paint_picture(n, target):
    print(row)