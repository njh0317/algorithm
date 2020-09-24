N,M = map(int, input().split())
ttokbbok = list(map(int, input().split()))
start = 0
end = max(ttokbbok)
result = 0


while(start<end):
    if(start>=end):
        break
    sum_height = 0
    mid = (start+end)//2
    for i in ttokbbok:
        sum_height +=(i-mid) if i>mid else 0
    if(sum_height>=M):
        result = mid
        start=mid+1
    else:
        end = mid-1

print(result)