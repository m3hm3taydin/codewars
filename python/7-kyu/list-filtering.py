def filter_list(l):
    results = []
    for i in l:
        if type(i) == int:
            results.append(i)
    return results
