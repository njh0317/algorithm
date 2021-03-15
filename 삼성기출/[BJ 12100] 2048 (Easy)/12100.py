import copy
max_block = 0
def remove_values_from_list(the_list):
   return [value for value in the_list if value != 0]
def one_line(arr):
    arr = remove_values_from_list(arr)
    moved_arr = []
    j = 0
    while(j<len(arr)):
        if(j+1==len(arr)):
            moved_arr.append(arr[j])
            j+=1
        elif(arr[j] == arr[j+1]):
            moved_arr.append(2*arr[j])
            j+=2
        else:
            moved_arr.append(arr[j])
            j+=1
    while(len(moved_arr)!=N):
        moved_arr.append(0)
    
    return moved_arr

def make_crash(direction, arr):
    moved_arr = [[0]*N for _ in range(N)]
    if(direction==0):
        for i in range(N):
            new_line = []
            for j in range(N):
                new_line.append(arr[j][i])
            new_line = one_line(new_line)
            for j in range(N):
                moved_arr[j][i] = new_line[j]
    if(direction==1):
        for i in range(N):
            new_line = []
            for j in range(N-1, -1, -1):
                new_line.append(arr[i][j])
            new_line = one_line(new_line)
            for j in range(N):
                moved_arr[i][j] = new_line[N-j-1]
    elif(direction==2):
        for i in range(N):
            new_line = []
            for j in range(N-1, -1, -1):
                new_line.append(arr[j][i])
            new_line = one_line(new_line)
            for j in range(N):
                moved_arr[j][i] = new_line[N-j-1]

    elif(direction==3):
        for i in range(N):
            new_line = []
            for j in range(N):
                new_line.append(arr[i][j])
            new_line = one_line(new_line)
            for j in range(N):
                moved_arr[i][j] = new_line[j]
    return moved_arr

def move_board(time, arr):
    if(time == 5):
        block = 0
        for i in range(N):
            for j in range(N):
                if(arr[i][j]!=0):
                    block = max(block, arr[i][j])
        global max_block
        max_block = max(max_block, block)
        return
    
    for i in range(4):
        #각 네 방향으로 움직여야 함
        #up, right, down, left
        temp = copy.deepcopy(arr)
        arr = make_crash(i, arr)
        move_board(time+1, arr)
        arr = temp

if __name__ == "__main__":
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    move_board(0, board)
    print(max_block)