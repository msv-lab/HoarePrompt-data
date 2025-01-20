def func_1(tiles):
    (t1, t2, t3) = tiles.split()

    def is_koutsu_or_shuntsu(t1, t2, t3):
        if t1 == t2 == t3:
            return True
        (n1, s1) = (int(t1[0]), t1[1])
        (n2, s2) = (int(t2[0]), t2[1])
        (n3, s3) = (int(t3[0]), t3[1])
        if s1 == s2 == s3 and sorted([n1, n2, n3]) in ([n1, n2, n3] for n1 in range(1, 8)):
            return True
        return False
    if is_koutsu_or_shuntsu(t1, t2, t3):
        return 0
    suits = {'m': [], 'p': [], 's': []}
    for tile in [t1, t2, t3]:
        suits[tile[1]].append(int(tile[0]))

    def tiles_needed_to_complete_group(tiles):
        tiles.sort()
        if len(tiles) == 1:
            return 2
        if len(tiles) == 2:
            if tiles[0] == tiles[1]:
                return 1
            if tiles[1] - tiles[0] <= 2:
                return 1
            return 2
        return 2
    min_additional_tiles = 2
    for (suit, numbers) in suits.items():
        min_additional_tiles = min(min_additional_tiles, tiles_needed_to_complete_group(numbers))
    return min_additional_tiles
input = sys.stdin.read
tiles = input().strip()
print(func_1(tiles))