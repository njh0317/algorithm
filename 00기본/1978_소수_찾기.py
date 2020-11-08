#제곱근 까지만 확인해보면 된다.
N = int(input())
number = list(map(int, input().split()))
check = 0
for i in range(N):
    flag = 0
    if(number[i]==1):
        continue
    for j in range(2,int(number[i]**0.5)+1):
        if(number[i]%j==0):
            flag = 1
            break
    if(flag == 0):
        check+=1
    flag = 0

print(check)