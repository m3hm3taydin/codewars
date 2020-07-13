def gcd(a,b):
    return a if not b else gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmapp(lst):
    if len(lst) == 2:
        return lcm(lst[0], lst[1])
    else:
        return lcm(lst[0], lcmapp(lst[1:]))




def convertFracts(lst):
    if len(lst) == 0:
        return []
    denom = [i[1] for i in lst]
    ans = []
    lcm = lcmapp(denom)
    for i in range(len(lst)):
        ans.append([lcm//denom[i]*lst[i][0],lcm])
    return ans
    

