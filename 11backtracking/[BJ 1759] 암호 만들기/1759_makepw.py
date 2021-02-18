vowel = ['a', 'e', 'i', 'o', 'u']
def check(arr):
    vcnt = 0

    for i in arr:
        if(i in vowel):
            vcnt+=1

    ccnt = len(arr) - vcnt
    if(vcnt>=1 and ccnt>=2):
        return True
    return False

def backtracking(arr, index, cnt):
    if(cnt == L):
        if(check(arr)):
            print(''.join(arr))
        return
    
    for i in range(index, C):
        if(visited[i] == False):
            visited[i] = True
            arr.append(char_list[i])
            backtracking(arr, i+1, cnt+1)
            arr.pop(-1)
            visited[i] = False

if __name__ == "__main__":
    L, C = map(int, input().split())
    char_list = list(input().split())
    char_list.sort()
    visited = [False]*C
    backtracking([], 0, 0)
