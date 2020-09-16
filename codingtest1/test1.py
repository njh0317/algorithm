import re
def solution(new_id):
    #1번째 단계 소문자로 치환
    no_capitals = new_id.lower()
    #2단계
    only_special_char = re.sub('[^a-z-_.0-9]', ' ', no_capitals)
    only_special_char = only_special_char.replace(" ","")
    print(only_special_char)
    #3단계 연속된 마침표 제거
    remove_dotdot = re.sub('[.]+', '.', only_special_char)
    print(remove_dotdot)
    #4단계 마지막 마침표 제거
    if(remove_dotdot.endswith(".")):
        remove_dotdot = remove_dotdot[:-1]
    if(remove_dotdot.startswith(".")):
        print("here")
        remove_dotdot = remove_dotdot[1:]
    print("1")
    print(remove_dotdot)
    if not remove_dotdot:
        remove_dotdot = 'a'
    print(remove_dotdot)
    if len(remove_dotdot)>=16:
        remove_dotdot = remove_dotdot[0:15]
    print(remove_dotdot)
    if(remove_dotdot.endswith(".")):
        remove_dotdot = remove_dotdot[:-1]
    
    print(remove_dotdot)
    if(len(remove_dotdot)<=2):
        final = remove_dotdot[-1]
        while(len(remove_dotdot)!=3):
            remove_dotdot = remove_dotdot+final
    print(remove_dotdot)
    return remove_dotdot


a=input()

print(solution(a))