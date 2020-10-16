N = int(input())
person = list(map(int, input().split()))
A, B = map(int, input().split())

num = 0

for i in range(N):
    if(person[i]<A):
        person[i] = 0
        num+=1
    else:
        person[i]-=A
        num+=1
    if(person[i]==0):
        continue
    num+=(person[i]//B+1) if person[i]%B!=0 else person[i]//B

print(num)
