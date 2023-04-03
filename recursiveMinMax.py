def Minimum(a, n):
    if(n==1):
        return a[0]
    else:
        return min(Minimum(a[1:], n-1), a[0])
def Maximum(a, n):
    if(n==1):
        return a[0]
    else:
        return max(Maximum(a[1:], n-1), a[0])
 
# Driver code
a = [10, 124, 45, 63, 1]
n = len(a)
print("Minimum element of array: ", Minimum(a, n))
print("Maximum element of array: ", Maximum(a, n))