def perimeter(n):
    n1, n2 = 1, 1
    count = 0
    sum = 0
    while count < n+1:
        sum += n1
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    return sum*4
