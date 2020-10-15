"""
이 아래에는 스택이 아닌 큐를 이용해서 위상 정렬을 해보겠다.
"""
adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}
def topological_sort_queue(adj_list):
    import queue

    myQue = queue.Queue()
    in_degree = [0] * len(adj_list)
    answer = []

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            temp = adj_list[j]
            for k in range(len(temp)):
                if temp[k] == i:
                    in_degree[i] += 1
    print("in_degree 배열: ", in_degree)

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            myQue.put(i)

    print("초기 스택: ", myQue)
    while not myQue.empty():
        node = myQue.get()
        answer.append(node)
        print("pop 된 노드: ", node)

        for i in range(len(adj_list[node])):
            idx = adj_list[node][i]
            in_degree[idx] -= 1
            if in_degree[idx] == 0:
                myQue.put(idx)

    print("answer: ", answer)


print(topological_sort_queue(adj_list))