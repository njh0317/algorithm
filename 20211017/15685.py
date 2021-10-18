dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

if __name__ == "__main__":
    N = int(input())

    arr = [[0]*101 for _ in range(101)]

    for n in range(N):
        x, y, d, g = map(int, input().split())
        dragon_curve = [[y, x]]
        nextx, nexty = x + dx[d], y + dy[d]
        dragon_curve.append([nexty, nextx])

        for i in range(g):
            last_idx = len(dragon_curve)-1
            standard_point = dragon_curve[last_idx] #y, x
            for idx in range(last_idx-1, -1, -1):
                origin_point = dragon_curve[idx]

                # 원래 점 - 기준 점 (y 변화량, x 변화량)
                change_len = [origin_point[0]-standard_point[0], origin_point[1] - standard_point[1]]

                new_pointy, new_pointx = standard_point
                new_point = [new_pointy, new_pointx]
                y_change = -1
                if(change_len[0]>0):
                    y_change = 3
                elif(change_len[0]<0):
                    y_change = 1
                
                if(y_change!=-1):
                    new_point[0]+= (abs(change_len[0])*dy[(y_change+3)%4])
                    new_point[1]+= (abs(change_len[0])*dx[(y_change+3)%4])
                x_change = -1
                if(change_len[1]>0):
                    x_change = 0
                elif(change_len[1]<0):
                    x_change = 2
                
                if(x_change!=-1):
                    new_point[0]+= (abs(change_len[1])*dy[(x_change+3)%4])
                    new_point[1]+= (abs(change_len[1])*dx[(x_change+3)%4])

                dragon_curve.append(new_point)
        for y, x in dragon_curve:
            arr[y][x] = 1
        
    answer = 0
    for i in range(100):
        for j in range(100):
            if(arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j] == 1 and arr[i+1][j+1] == 1):
                answer+=1
    
    print(answer)

