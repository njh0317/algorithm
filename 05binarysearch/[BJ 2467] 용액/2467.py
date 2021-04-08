if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if(arr[0]>=0):
        print(arr[0], arr[1])
    elif(arr[-1]<=0):
        print(arr[-2], arr[-1])
    else:
        left = 0
        right = N-1
        answer = float('inf')
        answerleft, answerright = 0, N-1
        while(left<right):
            if(abs(arr[left]+arr[right])<answer):
                answerleft, answerright = left, right
                answer = abs(arr[left]+arr[right])
            if(arr[left]+arr[right]>0):
                right-=1
            elif(arr[left]+arr[right]<0):
                left+=1
            else:
                answerleft = left
                answerright = right
                break
        print(arr[answerleft], arr[answerright])