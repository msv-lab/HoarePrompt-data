def count_tiles(tiles):
    tile_count = {}
    for tile in tiles:
        num, suit = tile[0], tile[1]
        if suit not in tile_count:
            tile_count[suit] = {}
        if num not in tile_count[suit]:
            tile_count[suit][num] = 0
        tile_count[suit][num] += 1
    return tile_count

def has_koutsu(tile_count):
    for suit in tile_count:
        for num in tile_count[suit]:
            if tile_count[suit][num] >= 3:
                return True
    return False

def has_shuntsu(tile_count):
    for suit in tile_count:
        nums = sorted([int(num) for num in tile_count[suit]])
        for i in range(len(nums) - 2):
            if nums[i] + 1 == nums[i+1] and nums[i+1] + 1 == nums[i+2]:
                return True
    return False

tiles = input().split()
tile_count = count_tiles(tiles)
if has_koutsu(tile_count) or has_shuntsu(tile_count):
    print(0)
else:
    print(1)
