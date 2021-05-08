def check_length_two(y1, x1, y2, x2, arr):
    if (y1 == y2):
        mid_x = (x1+x2)//2
        if(arr[y1][mid_x] == "X"):
            return True
        else:
            return False
    elif(x1 == x2):
        mid_y = (y1+y2)//2
        if(arr[mid_y][x1] == "X"):
            return True
        else:
            return False
    
    elif(y1<y2 and x1<x2):
        other_x1, other_y1 = min(x1, x2), max(y1, y2)
        other_x2, other_y2 = max(x1, x2), min(y1, y2)
        if (arr[other_y1][other_x1] == 'O' or arr[other_y2][other_x2] == 'O'):
            return False
        else:
            return True
    else:
        other_x1, other_y1 = min(x1, x2), min(y1, y2)
        other_x2, other_y2 = max(x1, x2), max(y1, y2)
        if (arr[other_y1][other_x1] == 'O' or arr[other_y2][other_x2] == 'O'):
            return False
        else:
            return True


def check_possible(person_list, arr):
    person_num = len(person_list)
    for i in range(person_num-1):
        for j in range(i+1, person_num):
            y1, x1 = person_list[i]
            y2, x2 = person_list[j]
            length = abs(y1-y2)+abs(x1-x2)
            if(length==1):
                return 0
            elif(length == 2):
                if not check_length_two(y1, x1, y2, x2, arr):
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        arr = []
        person_list = []
        for i in range(5):
            new_list = list(place[i])
            arr.append(new_list)
            for j in range(5):
                if(new_list[j] == 'P'):
                    person_list.append([i, j])
        answer.append(check_possible(person_list, arr))
    return answer

if __name__ == "__main__":
    place = [["PXPOO", "OOOPO", "OOOOO", "OOOOO", "OOOOO"]]
    print(solution(place))