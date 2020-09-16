money = int(input())
money = 1000-money
coinlist = [500, 100, 50, 10, 5, 1]
# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
num=0
for i in coinlist:
    num+=money//i
    money=money%i

print(str(num))