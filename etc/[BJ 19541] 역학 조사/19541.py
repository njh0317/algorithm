import copy
if __name__ == "__main__":
    N, M = map(int, input().split())
    meeting = []
    for i in range(M):
        meeting.append(list(map(int, input().split()))[1:])
    last = list(map(int, input().split()))
    last.insert(0, 0)
    
    reverse = copy.deepcopy(last)
    for i in range(M-1, -1, -1):
        people = meeting[i]
        check = 0
        for one in people:
            if(reverse[one] == 0):
                check = 1
                break
        
        if(check == 1):
            for one in people:
                reverse[one] = 0
    
    answer = copy.deepcopy(reverse)

    for i in range(0, M):
        people = meeting[i]
        check = 0
        for one in people:
            if(reverse[one] == 1):
                check = 1
                break
        if check == 1:
            for one in people:
                reverse[one] = 1
    flag = False
    for i in range(1, N+1):
        if(last[i]!=reverse[i]):
            flag = True
            break
    if(flag == True):
        print("NO")
    else:
        print("YES")
        for i in range(1, len(answer)):
            print(answer[i], end=" ")

