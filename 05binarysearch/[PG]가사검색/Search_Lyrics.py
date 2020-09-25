import re

def make_regular_exp(query):
    query = query.replace('?','.')
    #return "(?<!\S)"+query+"(?<!\S)"
    return query
def find_lyric(query, words):
    start = 0
    end = len(words)-1
    num = 0
    front_of_query = query.replace(".","")
    while start<=end:
        mid = (start+end)//2
        if(re.match(query,words[mid]) and len(query) == len(words[mid])):
            num+=1
            for i in range(mid+1,len(words)):
                if (re.match(query, words[i]) and len(query) == len(words[i])):
                    num+=1
                else:
                    break
            for i in range(mid-1, -1,-1):
                if (re.match(query, words[i]) and len(query) == len(words[i])):
                    num+=1
                else:
                    break

            break
        elif(query > words[mid]):
            start = mid + 1
        else : 
            end = mid - 1
    return num
        
array = [[] for _ in range(10001)]
array_reverse = [[] for _ in range(10001)]
def solution(words, queries):
    for i in words:
        array_reverse[len(i)].append(i[::-1])
        array[len(i)].append(i)
    
    for i in range(10001):
        array_reverse[i].sort()
        array[i].sort()
    answer = []
    #print("here")
    #print(reverse_words)
    for i in queries:
        now_query = make_regular_exp(i)
        if(now_query.startswith(".")):
            answer.append(find_lyric(now_query[::-1], array_reverse[len(now_query)]))
        else:
            answer.append(find_lyric(now_query, array[len(now_query)]))

    
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]

queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
words.sort()

print(solution(words,queries))

