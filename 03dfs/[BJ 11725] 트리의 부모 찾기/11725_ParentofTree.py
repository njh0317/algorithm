import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
flag = [-1 for _ in range(N+1)]

def dfs(num):
    now_tree = tree[num]
    for i in now_tree:
        if(flag[i]==-1):
            flag[i] = num
            dfs(i)
    return
for i in range(N-1):
    start, end = map(int,sys.stdin.readline().split())
    tree[start].append(end)
    tree[end].append(start)
flag[1] = 0
dfs(1)
for i in range(2, N+1):
    print(flag[i])