colorpaper = [0, 0]
#1 == blue, 0 == white
def check_square(length, starty, startx):
    first_num = arr[starty][startx]
    flag = False
    for i in range(starty, starty+length):
        for j in range(startx, startx+length):
            if(arr[i][j] != first_num):
                flag = True
                break
        if(flag == True):
            break
    if(flag == True):
        half_length = int(length/2)
        check_square(half_length, starty, startx)
        check_square(half_length, starty, startx + half_length)
        check_square(half_length, starty + half_length, startx)
        check_square(half_length, starty + half_length, startx + half_length)
    else:
        global colorpaper
        colorpaper[first_num]+=1

if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    
    check_square(N, 0, 0)
    print(colorpaper[0])
    print(colorpaper[1])