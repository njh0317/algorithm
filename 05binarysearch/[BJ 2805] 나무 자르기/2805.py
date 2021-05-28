if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    min_h, max_h = 0, max(tree)
    
    while(min_h<=max_h):
        mid_h = (min_h+max_h)//2
        sum_h = 0
        for t in tree:
            if(t>mid_h):
                sum_h+=(t-mid_h)
        
        if sum_h > M:
            if min_h == mid_h:
                break
            min_h = mid_h
        elif sum_h < M:
            max_h = mid_h
        else:
            break
    
    print(mid_h)

