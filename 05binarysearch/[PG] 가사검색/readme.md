# 프로그래머스 가사검색

## Algorithm

    이분탐색
    
## 코드 설명
1. make_regular_exp(query)


    + 나는 정규표현식을 썼기 때문에 하나의 문자로 대치해주는 .으로 바꿨다 
    
      + ( 근데 startswith 써도 되기 때문에 없애도 된다.)
    
    + 바꿀 쿼리를 하나씩 파라미터로 가져와 ?를 .으로 replace 한 문자열을 return 해준다.
   
   
2. find_lyric(query, words)

    + 해당하는 query와 match 되는 단어들을 이분탐색으로 찾는다.
    
    + words 는 query 의 길이와 동일한 단어들만 뽑아 sort 되어있는 리스트이다. 따라서 단어 길이 비교는 따로 필요 없다.
    
    + 주의할 점은 query에 해당하는 단어를 찾았다면 그 주위에 정답들이 존재한다는 말이기 때문에 해당 단어 앞, 뒤로 for문을 이용해 정답에 해당하는 단어가 있는지 확인해줘야한다.
    
    + 매치되는 단어가 존재할 때 마다 num을 증가시켜주고 return 해준다.
    
3. solution(words, queries)

    + array : 처음에 단어를 돌면서 단어 길이 별로 리스트를 만들어준다.
    
    + array_reverse : 반대로 할 때도 있기 때문에 단어를 반대로 돌려서 저장한 리스트도 만들어준다. ex)???o 
    
    + quries를 돌면서 find_lyric 호출
    
    + 정답을 append 한 답 return
    
## 결과

+ 정확성 18/18 모두 정답

+ 효율성 2/5 


## 느낀점
>
    효율성 고려해준다고 이분탐색을 했는데 모두 성공하지 못했다 ..
    
    아마 일부 맞은건 이분탐색을 썼기 때문에 리스트가 짧은 경우에 성공한 것 같다.
    
    완벽하지 못했던 이유는 단어개수만큼 for문을 돌았기 때문이 아닐까 싶다. 심지어 여러번
    
    (단어 개수로 리스트만들 때, 그 리스트 마다 다시 sort 해줄 때)
    
    검색해보니까 "트라이 자료구조" 를 사용하면 효율성도 모두 통과할 수 있다고 한다..
    
    이 후 해볼 과제로 남기도록 하겠다...
    
    
    
    
    
    
