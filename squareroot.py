
def squareroot(x):
    left = 1
    right = x 
    mid = 0
    while (left <= right):
        mid = (left + right) // 2 
        print('mid',mid)
        if mid * mid == x :
            return mid 
        elif mid * mid > x :
            right = mid - 1 
        else :
            left = mid + 1
            sqrt = mid 
    return sqrt
print(squareroot(25))