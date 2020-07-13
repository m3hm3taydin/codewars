def snail(snail_map):
    results = []

    while len(snail_map)>0:
        for s in snail_map[0]:
            results.append(s)
        snail_map.pop(0)

        snail_map = list(zip(*snail_map))[::-1]
        
    return results
