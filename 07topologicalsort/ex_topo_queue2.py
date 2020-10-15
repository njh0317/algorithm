#같은 위상 순서를 가진 것 끼리 묶어서 출력
#queue 사용
adj_list = {0: [2, 3], 1: [3, 4], 2: [3, 5], 3: [5], 4: [5], 5: []}

def queue_topo_sort(adj_list):
    queue = []
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
            queue.append(i)

    print("초기 큐: ", queue, "에서 반복 시작")
    while queue:
        print("\nqueue: ", queue)
        answer.append(queue)

        new_arr = []
        for i in queue:
            print(i, "에서 탐색 시작")
            for j in range(len(adj_list[i])):
                idx = adj_list[i][j]
                in_degree[idx] -= 1
                if in_degree[idx] == 0:
                    print("진입차수가 0이 된 정점: ", idx)
                    new_arr.append(idx)

        queue = new_arr

    print("answer: ", answer)


queue_topo_sort(adj_list)