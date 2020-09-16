
N,M,K = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
arr.reverse()
count = 0
add_num = 0
####첫번째 방법####
# while(True):
#     for i in range (0, K):
#         add_num+=arr[0]
#         count+=1
#         if(count==M):
#             break
#     add_num+=arr[1]
#     count+=1
#     if(count==M):
#         break

####두번째 방법 ####
repeatnum = K*arr[0]+arr[1]
K = K + 1

add_num = repeatnum*(M//K)+arr[0]*(M%K)


print(add_num)