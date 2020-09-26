import sys
def find_break_num(arr, h):

    start = 0
    end = len(arr)

    while(start<end):
        mid = (start+end)//2

        if(arr[mid]<h):
            start = mid + 1
        else:
            end = mid # 이 mid 가 정답일 가능성을 넣어줘야함 
    
    return end
N, H = map(int, input().split())
up = []
down = []
for i in range(N):
    input_list_2 = sys.stdin.readline().split()
    input_num = int(input_list_2[0])
    if i % 2 == 0:              #아래부터 높이 재기
        down.append(input_num)
    else:                       #위부터 높이 재기
        up.append(input_num)
down.sort()
up.sort()
es = len(down)
os = len(up)
lowest_num = N
num = 0
for i in range(1, H+1):
    aa = es - find_break_num(down, i)
    bb = os - find_break_num(up, H+1-i)
    answer = aa+bb
    if(lowest_num>answer):
        lowest_num = answer
        num = 1
    elif(lowest_num == answer):
        num+=1

print(str(lowest_num)+" "+str(num))

