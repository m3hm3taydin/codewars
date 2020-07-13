def find_multiples(integer, limit):
    
    start = 1
    results = []
    
    while limit >= integer*start:
        results.append(integer*start)
        start = start+1
    return results
