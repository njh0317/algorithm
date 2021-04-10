
if __name__ == "__main__":
    arr = input()
    stack = []  
    answer = ""
    for i in arr:
        if i.isalpha():
            answer+=i
        elif(i == "("):
            stack.append('(')
        elif(i == ")"):
            while(stack and stack[-1] != "("):
                answer+=stack.pop(-1)   
            stack.pop(-1)
        elif(i=="*" or i=="/"):
            while(stack and (stack[-1] == "*" or stack[-1] == "/")):
                answer+=stack.pop(-1)
            stack.append(i)
        else:
            while(stack and (stack[-1]!="(")):
                answer+=stack.pop(-1)
            stack.append(i)
    while(stack):
        answer+=stack.pop(-1)
    print(answer)

