if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    
    lis = [0]
    length = 0


    for num in arr:
        if num>lis[-1]:
            length+=1
            lis.append(num)
        else:
            start, end = 1, length
            while(start<end):
                mid = (start+end)//2
                if(lis[mid]<num):
                    start = mid+1
                else:
                    end = mid
            
            lis[start] = num
    
    print(length)




