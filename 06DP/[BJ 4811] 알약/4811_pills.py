import sys
if __name__ == "__main__":
    while True:
        N = int(sys.stdin.readline())
        if(N == 0):
            break
        number = [1]
        for i in range(N):
            num = 0
            for j in range(i+1):
                num+=number[i-j] * number[j]
            number.append(num)
        
        print(number[N])