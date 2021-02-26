def mod(num1, num2):
    if(num1 > num2):
        return num2, num1%num2
    else:
        return num1, num2%num1
if __name__ == "__main__":

    a, b = map(int, input().split())
    max_x = 0
    A, B = a, b
    while(True):
        A, B = mod(A, B)
        if(B==0):
            max_x = A
            break
    
    print(max_x)
    print(max_x*(a//max_x)*(b//max_x))

        