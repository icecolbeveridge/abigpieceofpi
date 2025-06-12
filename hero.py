import math, random, bisect

R = 2
R2 = R*R
xs = [0, R]
lengths = [R*2**0.5]
area = 0.5*R2 # we're starting with a triangle

def d(x1, x2):
    p1 = max(R2-x1**2 ,0.)
    p2 = max(R2-x2**2, 0.)
    d2 = 2 * (R2 - x1*x2 -(p1*p2)**0.5)
    return max(d2,0.)**0.5

def hero(x1, x2, x3, l31):
    l12 = d(x1,x2)
    l23 = d(x2,x3)
    s = (l12 + l23 + l31)*0.5
    A2 = max(s*(s-l12)*(s-l23)*(s-l31),0.)
    return A2**0.5, l12, l23 # return the lengths also

def loop(xs, lengths):
    x2 = random.random() * R
    index = bisect.bisect_left(xs, x2)
    x1 = xs[index-1]
    x3 = xs[index]
    l31 = lengths[index-1]
    da, l12, l23 = hero(x1,x2, x3, l31)
    xs.insert(index, x2)
    lengths[index-1] = l12
    lengths.insert(index, l23)
    return da, xs, lengths

for i in range(100000):
    da, xs, lengths = loop(xs, lengths)
    area += da
    print(i, area)
