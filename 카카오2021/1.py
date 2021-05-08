word_list = {"zero" : "0", "one" : "1", "two": "2", "three":"3", "four": "4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9" }
def solution(s):
    answer = 0
    for key, value in word_list.items():
        if key in s:
            s = s.replace(key, value)
    answer = int(s)
    return answer

if __name__ == "__main__":
    s = ["one4seveneightsevenseven","23four5six7","2three45sixseven","123"]

    for i in s:
        print(solution(i))