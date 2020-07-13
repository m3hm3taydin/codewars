def find_outlier(integers):
    odds = 0
    evens = 0
    for integer in integers[:3]:
        if integer % 2 == 0 : 
            evens = evens + 1
        else:
            odds = odds + 1
    
    val = 1 if odds < evens else 0
    return [integer for integer in integers if integer % 2 == val][0]
    #return [integer for integer in integers if integer % 2 == sum(integers) % 2][0]
