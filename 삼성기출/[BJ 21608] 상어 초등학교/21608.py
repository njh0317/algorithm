dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
info = {}
score = {0:0, 1:1, 2:10, 3:100, 4:1000}
def isin(y, x):
    if 0<=y<N and 0<=x<N:
        return True
    return False
def find_sit(friend_list):
    candidate_list = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=0:
                continue
            empty_num = 0
            friend_num = 0
            for k in range(4):
                nexty, nextx = i+dy[k], j+dx[k]
                if(isin(nexty, nextx)):
                    if(arr[nexty][nextx]==0):
                        empty_num+=1
                    if(arr[nexty][nextx] in friend_list):
                        friend_num+=1
            candidate_list.append([friend_num, empty_num, i, j])
    candidate_list.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    return candidate_list[0]
def check_score():
    answer = 0
    for i in range(N):
        for j in range(N):
            per_num = arr[i][j]
            f_list = info[per_num]
            f_n = 0
            for k in range(4):
                nexty, nextx = i+dy[k], j+dx[k]
                if(isin(nexty, nextx)):
                    if(arr[nexty][nextx] in f_list):
                        f_n+=1
            answer+=score[f_n]
    return answer

if __name__ == "__main__":
    N = int(input())
    people_num = N**2
    arr = [[0]*N for _ in range(N)]
    
    for i in range(people_num):
        a, *b = map(int, input().split())
        info[a] = b
        temp = find_sit(b)
        f_n, e_n, y, x = temp
        arr[y][x] = a
    
    print(check_score())


