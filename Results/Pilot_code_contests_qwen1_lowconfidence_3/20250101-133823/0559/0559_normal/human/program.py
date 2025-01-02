input = raw_input

h, w = map(int, input().split(" "))

meiro = []
coords = []
for i in range(h):
    line = list(input())
    cur_coords = [(j, i) for j in range(w) if line[j] == "."]
    coords += cur_coords
    meiro.append(line)

graphs = []
graph = {}
for cur_coord in coords:
    x, y = cur_coord
    tugi_kouhos = [(x+dx, y) for dx in [-1, 1] if 0 <= x+dx < w]
    tugi_kouhos += [(x, y+dy) for dy in [-1, 1] if 0 <= y+dy < h]
    childs = []
    for tugi_kouho in tugi_kouhos:
        if tugi_kouho in coords:
            childs.append(tugi_kouho)
    graph[cur_coord] = childs


depth_dict_org = {}
for coord in coords:
    depth_dict_org[coord] = None

def calc_depth(coord1, coord2):
    depth_dict = depth_dict_org.copy()

    cur_coord = coord1
    end_coord = coord2
    cur_depth = 0
    used_coords = [coord1]

    childs = graph[coord1]
    while len(childs) != 0:
        cur_depth += 1
        next_childs = []
        used_coords += childs
        for child in childs:
            res = get_childs(child, coord2, used_coords)
            #print("child", child, res)
            #print(used_coords)
            if res == "found":
                return cur_depth + 1
            next_childs += res

        childs = list(set(next_childs))
        #print(childs)

    return 0

def get_childs(jibun, target, used_coords):
    
    childs = []
    for child in graph[jibun]:
        if child == target:
            return "found"
        if child not in used_coords:
            childs.append(child)
    return childs
       

n_coords = len(coords)
max_depth = 0
for i in range(n_coords):
    coord1 = coords[i]
    for j in range(i+1, n_coords):
        coord2 = coords[j]
        cur_depth = calc_depth(coord1, coord2)
        #print(coord1, coord2, cur_depth)
        max_depth = max(max_depth, cur_depth)

print(max_depth)