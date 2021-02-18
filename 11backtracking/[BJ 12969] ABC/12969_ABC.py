import sys
char_list = ['A','B','C']
def check(arr):
    cnt = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if(arr[i]<arr[j]):
                cnt+=1

    return cnt

def backtracking(arr, choose_num, acnt, bcnt, ccnt):
    if(choose_num == N):
        if(check(arr) == K and acnt!=0 and bcnt!=0 and ccnt!=0):
            print("".join(arr))
            sys.exit()
        return

    for i in range(3):
        arr.append(char_list[i])
        if(char_list[i] == 'A'):
            backtracking(arr, choose_num+1, acnt+1, bcnt, ccnt)
        elif(char_list[i] == 'B'):
            backtracking(arr, choose_num+1, acnt, bcnt+1, ccnt)
        else:
            backtracking(arr, choose_num+1, acnt, bcnt, ccnt+1)

        
        arr.pop(-1)

    



if __name__ == "__main__":
    N, K = map(int, input().split())
    backtracking([], 0, 0, 0, 0)
    print(-1)