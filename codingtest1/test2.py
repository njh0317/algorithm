from itertools import combinations
def solution(orders, course):
    answer = []
    new_orders = []

    for i in orders:
        new_orders.append(list(i))
        #print(i)
    r_answer = []
    combi = []
    for i in new_orders:
        combi_list_num = len(new_orders)
        for j in range(0, combi_list_num-1):
            for k in range(j+1, combi_list_num):
                now_result = list(set(new_orders[j]).intersection(new_orders[k]))
                now_result = sorted(now_result)
                if(len(now_result) in course and now_result not in r_answer):
                    print(str(j)+" "+str(k))
                    print(now_result)
                    r_answer.append(now_result)
                    a = input()

    for i in r_answer:
        answer.append("".join(i))
    answer = sorted(answer)
    return answer



orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]

print(solution(orders,course))