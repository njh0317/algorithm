arr1 = [0,0,-1,1]
arr2 = [-1,1,0,0]
#L, R, U, D
move_type = ['L', 'R', 'U', 'D']
def check_move(move_char):
    if(move_char == 'L'):
        return 0
    elif(move_char == 'R'):
        return 1
    elif(move_char == 'U'):
        return 2
    elif(move_char == 'D'):
        return 3

N = input()
move_plan = list(input().split())

a = 1
b = 1

for i in move_plan:
    #move_num = check_move(i)
    if not(a+arr1[move_type.index(i)]>int(N) or a+arr1[move_type.index(i)]<1 or b+arr2[move_type.index(i)]>int(N) or b+arr2[move_type.index(i)]<1):
        a = a + arr1[move_type.index(i)]
        b = b + arr2[move_type.index(i)]
print(str(a)+" "+str(b))


