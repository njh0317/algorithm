N = int(input())
number = list(map(int, input().split()))

new_list = [number[0]]
result = 1
for i in number:

    if(i>new_list[-1]):
        new_list.append(i)
        result+=1
    else:
        start = 0
        end = len(new_list)

        while(start<end):
            mid = (start+end)//2
            if(new_list[mid]<i):
                start = mid + 1
            else:
                end = mid

        new_list[start] = i
        
print(result)   