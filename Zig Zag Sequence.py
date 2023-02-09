def findZigZagSequence(a, n):
    a.sort()
    m=n
    mid = int(n/2)
    a[mid], a[m-1] = a[m-1], a[mid]
    mid=mid+1
    m=m-2
    while(mid <= m):
        a[mid], a[m] = a[m], a[mid]
        mid = mid + 1
        m = m - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a,n)



