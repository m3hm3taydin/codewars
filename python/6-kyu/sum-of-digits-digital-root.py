def digital_root(n):
    val = str(sum([int(s) for s in str(n)]))
    return int(val) if len(val) == 1 else digital_root(int(val))
