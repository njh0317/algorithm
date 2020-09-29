N = int(input())
number = list(map(int, input().split()))
newnum =[]
newnum.append(number[0])
flag = 0
for i in range(1, N):
    checklist = []
    for j in range(i-1, -1, -1):
        if(number[i]>number[j]):
            checklist.append(newnum[j])
            flag = 1

    if(flag == 0):
        newnum.append(number[i])
    else:
        flag = 0
        newnum.append(max(checklist)+number[i])

#print(newnum)
print(max(newnum))
