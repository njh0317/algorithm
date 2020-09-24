def make_router(distance):
    now_point = router[0]
    num_of_router = 1
    
    for i in range(1, len(router)):
        if(router[i]-now_point>=distance):
            num_of_router+=1
            now_point = router[i]
    return num_of_router

def find_largest_distance(target):
    start = 1
    end = router[-1]
    
    while start<=end:
        mid = (start+end)//2
        if(target<=make_router(mid)):
            start = mid+1
            result = mid
        else:
            end = mid-1
    return result


N,C = map(int, input().split())
router = []
for i in range(0, N):
    router.append(int(input()))

router.sort()

print(find_largest_distance(C))