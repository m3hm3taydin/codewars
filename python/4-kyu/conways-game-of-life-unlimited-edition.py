def get_data(cells, x, y):#check_out_of_limit
    try:
        # check for negative index
        if x<0 or y<0:
            return 0
        return cells[x][y]
    except:
        return 0
def get_live_neighbour_count(cells, index):
    return get_data(cells,index[0]-1,index[1])\
            + get_data(cells, index[0]+1,index[1])\
            + get_data(cells, index[0]-1, index[1]-1)\
            + get_data(cells, index[0]-1, index[1]+1)\
            + get_data(cells, index[0]+1, index[1]-1)\
            + get_data(cells, index[0]+1, index[1]+1)\
            + get_data(cells, index[0], index[1]-1)\
            + get_data(cells, index[0], index[1]+1)
def is_it_live(cells, index):
    return True if cells[index[0]][index[1]] == 1 else False

def generae_one_tick(cells):
    results = []
    for (idx, cell_line) in enumerate(cells):
        result_line = []
        for (idy, cell) in enumerate(cell_line):
            count = get_live_neighbour_count(cells, [idx,idy])
            #print('count : {} - x {}, y {}'.format(count, idx, idy))
            alive = is_it_live(cells, [idx,idy])
            if alive and count < 2:
                #print('{}-{} dies underpopulation'.format(idx, idy))
                result_line.append(0)
            elif alive and count > 3:
                #print('{}-{} dies overcrowding'.format(idx, idy))
                result_line.append(0)
            elif alive and (count == 2 or count==3):
                #print('{}-{} lives next generation'.format(idx, idy))
                result_line.append(1)
            elif not alive and count == 3:
                #print('{}-{} becomes a live cell'.format(idx, idy))
                result_line.append(1)
            else:
                #print('dies')
                result_line.append(0)
        results.append(result_line)
    return results
    

def transpose(cells):
    return list(zip(*cells))[::-1]


def create_dummy_zeros(cells):
    for i in range(4):
        cells.append([0] * len(cells[0]))
        cells = transpose(cells)
    return cells

def clear_zeros(cells):
    for i in range(8):
        #for (idx, r) in enumerate(cells):
        #if sum(r) == 0:
        if sum(cells[0]) == 0:
            print('removeing')
            cells.pop(0)
        cells = transpose(cells)
    return cells

    
def get_generation(cells, generations):
    ch = cells.copy()
    for i in range(generations):
        print('-- generation {} --'.format(i))
        # create dummy zero lines every side for moves
        ch = create_dummy_zeros(ch)
        ch = generate_one_tick(ch)
        # clear zeros before next generation
        ch = clear_zeros(ch)

    # convert tuple to array
    print(ch)
    ch = clear_zeros(ch)

    result = [list(x) for x in ch]
    print(result)

    return resultt
