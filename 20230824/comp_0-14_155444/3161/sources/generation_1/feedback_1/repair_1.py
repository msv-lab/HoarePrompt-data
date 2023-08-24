from typing import List

def count_differences(picture: List[List[int]], target: List[List[int]]) -> int:
    n = len(picture)
    count = 0
    for i in range(n):
        for j in range(n):
            if picture[i][j] != target[i][j]:
                count += 1
    return count

def paint_picture(n: int, target: List[List[int]]) -> List[str]:
    picture = [['0'] * n for _ in range(n)]
    if n == 1:  # base case
        picture[0][0] = str(target[0][0])
    else:
        split = n // 2
        sub_target = [row[:split] for row in target[:split]]  # top-left sub-picture
        sub_picture = paint_picture(split, sub_target)  # paint the top-left sub-picture
        for i in range(split):  # copy the painted top-left sub-picture to the main picture
            for j in range(split):
                picture[i][j] = sub_picture[i][j]
        
        for i in range(split, n):  # paint the other sub-pictures
            sub_picture = paint_picture(split, target[split:])
            for j in range(split):
                picture[i][j] = sub_picture[i - split][j]
        
        for j in range(split, n):  # paint the remaining sub-pictures
            sub_picture = paint_picture(split, [row[split:] for row in target[:split]])
            for i in range(split):
                picture[i][j] = sub_picture[i][j - split]
    
    return ["".join(row) for row in picture]

n = int(input())
target = [list(map(int, input())) for _ in range(n)]

#print(target)

print(count_differences(paint_picture(n, target), target))
for row in paint_picture(n, target):
    print(row)