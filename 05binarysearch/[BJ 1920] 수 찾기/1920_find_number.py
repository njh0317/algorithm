def isthere(start, end, target, A):
    if(start>end):
        return 0
    mid = (start + end)//2

    if(A[mid] == target):
        return 1
    if(A[mid]>target):
        end = mid - 1
    elif(A[mid]<target):
        start = mid + 1
    return isthere(start, end, target, A)

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
A.sort()
for i in B:
    print(isthere(0, len(A)-1, i, A))
