max_num = 0
min_num = 0
flag = False
def calculate(option, num1, num2):
    if(option == 0):
        return num1 + num2
    elif(option == 1):
        return num1 - num2
    elif(option == 2):
        return num1*num2
    else:
        if(num1<0):
            return (-1*num1)//num2 *(-1)
        else:
            return num1//num2

def backtracking(index, num_list, nownum):
    if(index == N):
        global flag
        global max_num, min_num
        if(not flag):
            max_num = nownum
            min_num = nownum
            flag = True
            return

        max_num = max(max_num, nownum)
        min_num = min(min_num, nownum)
        return
    
    for i in range(4):
        if(num_list[i]!=0):
            num_list[i]-=1
            backtracking(index+1, num_list, calculate(i, nownum, number[index]))
            num_list[i]+=1
    return
        


if __name__ == "__main__":
    N = int(input())
    number = list(map(int, input().split()))
    #덧셈, 뺄셈, 곱셈, 나눗셈
    operator = list(map(int, input().split()))
    backtracking(1, operator, number[0])
    print(max_num)
    print(min_num)