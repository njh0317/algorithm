R,C,M = map(int, input().split())
shark_loc = []
shark_info = []
dc = [0,0,0,1,-1]
dr = [0,-1,1,0,0]

for i in range(M):
    new_shark = list(map(int, input().split()))
    shark_loc.append([new_shark[0],new_shark[1]])
    shark_info.append([new_shark[2],new_shark[3],new_shark[4]])
def change_dir(d):
    if(d == 1 or d == 2):
        return 2 if(d == 1) else 1
    else:
        return 3 if(d == 4) else 4
def change_loc(r,c,s,d,z):
    for i in range(s):
        nextr = r + dr[d]
        nextc = c + dc[d]

        if(nextr == 0 or nextc == 0 or nextr == R+1 or nextc == C+1):
            d = change_dir(d)
            nextr = r + dr[d]
            nextc = c + dc[d]
        r = nextr
        c = nextc
    
    return r,c,s,d,z



if __name__ == "__main__":
    catch_size = 0
    for i in range(1, C+1):
        min_shark = R+1
        shark = -1
        for j in range(0, M):
            if(shark_loc[j][1] == i and shark_loc[j][0] < min_shark):
                min_shark = shark_loc[j][0]
                shark = j

        if(shark != -1):#해당 위치에 상어가 있었다면
            catch_size += shark_info[shark][2]
            del shark_loc[shark]
            del shark_info[shark]
            M-=1 #상어 한마리 줄어듦
        new_loc = []
        new_info = []
        for j in range(M):
            r,c,s,d,z = change_loc(shark_loc[j][0], shark_loc[j][1], shark_info[j][0], shark_info[j][1], shark_info[j][2])#r,c,속력, 방향 가져감
            if([r,c] in new_loc):
                find_index = new_loc.index([r,c])
                if(z>new_info[find_index][2]):
                    new_info[find_index][0] = s
                    new_info[find_index][1] = d
                    new_info[find_index][2] = z
            else:
                new_loc.append([r,c])
                new_info.append([s,d,z])
        shark_loc = new_loc
        shark_info = new_info
        M = len(shark_loc)
    print(catch_size)