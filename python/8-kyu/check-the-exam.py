def check_exam(arr1,arr2):
    result = sum([4 if val == arr2[idx] else 0 if not arr2[idx] else -1 for idx, val in enumerate(arr1)])
    return 0 if result < 0 else result 
