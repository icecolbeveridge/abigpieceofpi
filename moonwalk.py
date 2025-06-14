# simulate an n-step random moonwalk to calculate pi
import math, random

def hit_rate(func, n = 1000):
    """Wrapper function to test convergence to 2dp, 3dp and 4dp.
    3dp is generously "between 3.1405 and 3.1425" to make the interval
    more symmetric. """
    h2 = 0
    h3 = 0
    h4 = 0
    print("Iter |  2dp%  |  3dp%  |  4dp%  | Result  ")
    print("-----|--------|--------|--------|---------")
    for i in range(n):
        f = func()
        h2 += 1 if 3.135 <= f < 3.145 else 0
        h3 += 1 if 3.1405 <= f < 3.1425 else 0
        h4 += 1 if 3.14145 <= f < 3.14155 else 0
        print(f"{i+1:4d} | {100*h2/(i+1):6.2f} | {100*h3/(i+1):6.2f} | {100*h4/(i+1):6.2f} | {f:8.6f}" )
    return 100*h2/n, 100*h3/n, 100*h4/n


def marsaglia():
    """Marsaglia's method to generate a random point on the surface of a sphere."""
    a,b = random.random() * 2 - 1, random.random() * 2 - 1
    while a**2 + b**2 > 1:
        a,b = random.random() * 2 - 1, random.random() * 2 - 1
    r = (1 - a**2 - b**2)**0.5
    x = 2*a*r
    y = 2*b*r
    z = 1-2*(a**2 + b**2)
    return (x,y,z)

SQRT_HALF = math.sqrt(0.5)
def rand_in_circle(discrete=False):
    """Generate a random point on a unit circle. If the discrete flag is set, the "circle" consists of four points (NE, NW, SW, SE).
    """
    if discrete:
        r1=random.choice([SQRT_HALF, -SQRT_HALF])
        r2=random.choice([SQRT_HALF, -SQRT_HALF])
        return(r1,r2)
    r1 = random.random()*2 - 1
    r2 = random.random()*2 - 1
    r = r1*r1 +r2*r2
    if r >= 1:
        return rand_in_circle()
    r = math.sqrt(r)
    return (r1/r,r2/r)

def normalise(x, y=None, z=None):
    """Normalise a vector"""
    if type(x)==type((1,2,3)):
        x,y,z=x
    d = math.sqrt(x**2 + y**2 + z**2)
    return x/d, y/d, z/d

def random_step(p, e = 0.01, discrete = False):
    """Take a step of size e in a random direction tangent to the sphere at p."""
    x,y,z = p

    # set up basis for tangent plane
    dx1, dy1, dz1 = normalise(y-z, z-x, x-y)

    s = x+y+z
    dx2, dy2, dz2 = normalise(s*x-1, s*y-1, s*z-1)

    r1, r2 = rand_in_circle(discrete = discrete)

    dx = e*(r1*dx1 + r2*dx2)
    dy = e*(r1*dy1 + r2*dy2)
    dz = e*(r1*dz1 + r2*dz2)
    return normalise(x+dx, y+dy, z+dz)


def moonwalk(n=1_000_000, e=0.1, discrete=False):
    """Perform a random walk on a sphere, n steps of size e.
    Calculate the distance of each point on the walk from the three
    axes, and use these to approximate pi.
    """
    rs = 0.
    x,y,z = marsaglia()
    for _ in range(n):
        # adjust x, y, z slightly in a tangent plane
        x,y,z = random_step((x,y,z), e=e, discrete=discrete)
        rs += math.sqrt(x**2 + y**2) + math.sqrt(y**2+z**2) + math.sqrt(z**2+x**2)
    return (4*rs)/(3*n)

if __name__=="__main__":
    hit_rate(moonwalk)
