if __name__ == "__main__":
    N = int(input())
    building = []
    for i in range(N):
        building.append(int(input()))   
    answer = 0
    stack = []
    for start in range(len(building)):
        while(stack and stack[-1]<=building[start]):
            stack.pop(-1)
        answer+=len(stack)
        stack.append(building[start])
    print(answer)
