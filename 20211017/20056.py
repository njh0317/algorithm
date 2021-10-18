dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
def make_key(num1, num2):
    return str(num1)+" "+str(num2)
def solve_key(key_str):
    k1, k2 = map(int, key_str.split())
    return k1, k2

def move_fireball(fireball_list, K, N):
    # 파이어볼 이동 (K 번 이동)
    # 1. 파이어볼 d로 s만큼 이동, (같은 칸에 여러 개의 파이어볼 있을 수 있음)
    # 2. 이동 후 2개 이상의 파이어볼 경우
    #   1. 하나로 합쳐짐 -> 4개로 나뉨
    #   2. 질량 : (질량 합)/5, 속력 (속력 합 / 파이어볼 개수)
    #   3. 방향이 모두 홀수 혹은 짝수이면 0, 2, 4, 6/ 그렇지 않으면 1, 3, 5, 7
    #   4. 질량이 0이면 소멸 
    for k in range(K):
        move_position = {}

        for idx, fireball in enumerate(fireball_list):
            y, x, m, s, d = fireball
            nexty, nextx = (y + dy[d]*s + N)%N, (x + dx[d]*s + N)%N
            position_key = make_key(nexty, nextx)
            if(position_key in move_position.keys()):
                move_position[position_key].append(idx)
            else:
                move_position[position_key] = [idx]
        new_fireball_list = []
        for k, v in move_position.items():
            y, x = solve_key(k)
            if(len(v) == 1):
                fireball_idx = v[0]
                origin_fireball = fireball_list[fireball_idx]

                new_fireball_list.append([y, x, origin_fireball[2], origin_fireball[3], origin_fireball[4]])
            else:
                same_type = fireball_list[v[0]][4]%2 #짝수이면 0 홀수이면 1
                flag = True # 모두 같은 타입일 경우 True, 그렇지 않으면 False
                total_weight, total_speed = 0, 0
                fireball_num = len(v)
                for fireball_idx in v:
                    origin_fireball = fireball_list[fireball_idx]
                    total_weight += origin_fireball[2]
                    total_speed += origin_fireball[3]
                    if(origin_fireball[4]%2 != same_type):
                        flag = False
                
                new_weight = total_weight // 5
                new_speed = total_speed // fireball_num

                if(new_weight != 0):
                    if(flag):
                        startdir = 0
                    else:
                        startdir = 1
                    
                    for i in range(4):
                        new_fireball_list.append([y, x, new_weight, new_speed, startdir])
                        startdir+=2
        fireball_list = new_fireball_list

    total_weight = 0
    for f in fireball_list:
        total_weight+=f[2]
    return total_weight

if __name__ == "__main__":
    # 마법사 상어가 크기가 N*N 인 격자에 파이어볼 M 개 발사
    # i -> (r, c) 질량 m 방향 d 속력 s
    # N*N 격자 -> 1~N 번, 1번 행, N번 행 연결

    N, M, K = map(int, input().split())
    fireball_list = []
    for i in range(M):
        r, c, m, s, d = map(int, input().split())
        fireball_list.append([r-1, c-1, m, s, d])


    print(move_fireball(fireball_list, K, N))


    

