#fail
import copy
min_time = 0
def init(n):
    graph = {}
    reverse_graph = {}
    for i in range(n):
        graph[i+1] = {}
        reverse_graph[i+1] = {}
    
    return graph, reverse_graph

def backtracking(road, reversed_road, now_n, end, traps, time, n, visited, visited_trap_list):
    if now_n == end:
        global min_time
        if min_time == 0:
            min_time = time
        else:
            min_time = min(min_time, time)
        return
    
    if now_n in traps:
        visited[now_n]+=1
    for k, v in road[now_n].items():
        change_time = 0
        if now_n in traps and k in traps:
            if [now_n, k] not in visited_trap_list:
                visited_trap_list.append([now_n, k])
            else:
                continue
        if(now_n in traps):
            change_time += visited[now_n]
        if k in traps:
            change_time += visited[k]
        if change_time%2 == 0:
            backtracking(road, reversed_road, k, end, traps, time+v, n, visited, visited_trap_list)
        if now_n in traps and k in traps:
            if [now_n, k] in visited_trap_list:
                visited_trap_list.pop(-1)
    for k, v in reversed_road[now_n].items():
        if now_n in traps and k in traps:
            if [now_n, k] not in visited_trap_list:
                visited_trap_list.append([now_n, k])
            else:
                continue
        change_time = 0
        if(now_n in traps):
            change_time += visited[now_n]
        if k in traps:
            change_time += visited[k]
        if change_time%2 == 1:
            backtracking(road, reversed_road, k, end, traps, time+v, n, visited, visited_trap_list)
        if now_n in traps and k in traps:
            if [now_n, k] in visited_trap_list:
                visited_trap_list.pop(-1)

    if now_n in traps:
        visited[now_n]-=1
    return
def solution(n, start, end, roads, traps):
    global min_time
    min_time = 0
    answer = 0
    graph, reversed_graph = init(n)
    visited = {}
    for i in traps:
        visited[i] = 0
    for i in roads:
        P, Q, S = i
        if Q in graph[P].keys():
            graph[P][Q] = min(S, graph[P][Q])
            reversed_graph[Q][P] = min(S, reversed_graph[Q][P])
        else:
            graph[P][Q] = S
            reversed_graph[Q][P] = S

    backtracking(graph, reversed_graph, start, end, traps, 0, n, visited, [])
    answer = min_time
    return answer


if __name__ == "__main__":
    n = [3, 4]
    end = [3, 4]
    roads = [[[1, 2, 2], [3, 2, 3]], [[1, 2, 1],[3, 2, 1], [2, 4, 1]]]
    traps = [[2], [2, 3]]
    print(solution(n[1], 1, end[1], roads[1], traps[1]))
    # for i in range(2):
    #     print(solution(n[i], 1, end[i], roads[i], traps[i]))
