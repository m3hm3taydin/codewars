def fib(nterms):
    n1, n2 = 0, 1
    count = 0
    
    results = []

    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        results = [n1, n2]
        count += 1
    
    return results
            
def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    elif prod == 1: 
        return [1, 1, True]
    elif prod == 2:
        return [1, 2, True]


    n = 1
    while True:
        if fib(n)[0]*fib(n)[1] > prod:
            res = fib(n)
            res.append(False)
            return res
        elif fib(n)[0]*fib(n)[1] == prod:
            res = fib(n)
            res.append(True)
            return res
        n += 1

