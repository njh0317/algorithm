def ccw(x, y, z):
    S = x[0]*y[1]+y[0]*z[1]+z[0]*x[1]-(x[1]*y[0]+y[1]*z[0]+z[1]*x[0])
    if(S>0): return 1
    elif(S==0): return 0
    else: return -1
def isIntersect(line1, line2):
    a = line1[0]
    b = line1[1]
    c = line2[0]
    d = line2[1]

    ab = ccw(a, b, c)*ccw(a, b, d)
    cd = ccw(c, d, a)*ccw(c, d, b)
    if(ab == 0 and cd == 0):
        if(a>b): a, b = b, a
        if(c>d): c, d = d, c
        return a<=d and c<=b
    return ab<=0 and cd<=0
if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    flag1 = isIntersect([[x1, y1], [x2, y2]], [[x3, y3],[x4, y4]])
    if(flag1):
        print(1)
    else:
        print(0)
