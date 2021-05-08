def save_up_down(n):
    save = {}
    for i in range(n):
        down, up = i-1, i+1
        if(up == n):
            up = -1
        save[i] = [down, up]
    return save

def solution(n, k, cmd):
    answer = ''
    delete_list = [] #stack 형식 
    state = [True]*n #삭제 됐는지 여부 표시
    now_k = k
    save = save_up_down(n)
    for command in cmd:
        if(command == 'C'):
            state[now_k] = False
            delete_list.append(now_k)
            down, up = save[now_k]
            if(down != -1) :
                save[down][1] = up
            if(up != -1):
                save[up][0] = down
        
            now_k = up
            if(now_k == -1):
                now_k = down
            
        elif(command == 'Z'):
            restore_k = delete_list.pop(-1)
            state[restore_k] = True
            down, up = save[restore_k]
            if down != -1:
                save[down][1] = restore_k
            if up != -1:
                save[up][0] = restore_k

        else:
            c, x = command.split()
            if c == 'U':
                for i in range(int(x)):
                    now_k = save[now_k][0]
            else: #D
                for i in range(int(x)):
                    now_k = save[now_k][1]


    for i in state:
        if(i):
            answer+='O'
        else:
            answer+='X'

    return answer

if __name__ == "__main__":
    cmd = [["D 2","C","U 3","C","D 4","C","U 2","Z","Z"],["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]]

    for i in cmd:
        print(solution(8, 2, i))