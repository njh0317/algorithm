def check_possibility(start, end, word_len):
    count = 0
    for i in range(word_len):
        if start[i] != end[i]:
            count+=1
        if(count>1):
            return False
    if(count == 1):
        return True
    else:
        return False

def make_graph(words, length, word_num):
    graph = {}
    for w in words:
        graph[w] = []

    for i in range(word_num-1):
        for j in range(i+1, word_num):
            if(check_possibility(words[i], words[j], length)):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    return graph

def bfs(begin, target, graph, word_num):

    visited = {w:-1 for w in graph}
    visited[begin] = 1
    queue = []
    queue.append(begin)

    while(queue):
        vertex = queue.pop(0)
        count = visited[vertex]
        for w in graph[vertex]:
            if visited[w]==-1:
                if(target == w):
                    return count+1
                visited[w] = count+1
                queue.append(w)
    return 0



def solution(begin, target, words):
    answer = 0
    length = len(begin)
    word_num = len(words)
    graph = make_graph(words, length, word_num)
    print(graph)
    for w in words:
        if(check_possibility(begin, w, length)):
            if(w == target):
                return 1
            count = bfs(w, target, graph, word_num)
            if(count != 0):
                if answer == 0:
                    answer = count
                else:
                    answer = min(answer, count)
    return answer

begin = "hot"
target = "lot"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))