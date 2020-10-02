N = int(input())
wine = [0]
for i in range(N):
    wine.append(int(input()))
wine_max = [0,wine[1]]

if(N>1):
    wine_max.append(wine[1]+wine[2])

    for i in range(3, N+1):
        find_max = 0
        wine_max.append(max((wine[i]+wine[i-1]+max(wine_max[:i-2])), (wine[i]+max(wine_max[:i-1]))))
print(max(wine_max))