def find(position):
    queue = []
    queue.append([position, 0])
    visited = [False]*100001
    visited[position] = True
    while(queue):
        now_position, time = queue.pop(0)
        if(now_position-1>=0):
            if(not visited[now_position-1]):
                if(now_position-1 == K):
                    return time+1
                queue.append([now_position-1, time+1])
                visited[now_position-1] = True
        if(now_position*2<100001):
            if(not visited[now_position*2]):
                if(now_position*2 == K):
                    return time+1
                queue.append([now_position*2, time+1])
                visited[now_position*2] = True
        if(now_position+1<100001):
            if(not visited[now_position+1]):
                if(now_position+1 == K):
                    return time+1
                queue.append([now_position+1, time+1])
                visited[now_position+1] = True


            
if __name__ == "__main__":
    N, K = map(int, input().split())
    if(N == K):
        print(0)
    else:
        print(find(N))