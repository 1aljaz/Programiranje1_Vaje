EPS = 1e-9

class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def andrew_monotone_chain(points):
    unique_points = list({(p.x, p.y) for p in points})
    unique_points = [Point(x, y) for x, y in unique_points]
    points = sorted(unique_points)

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= EPS:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= EPS:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1] 
    return hull

def area_of_polygon(points):
    area = 0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i].x * points[j].y - points[i].y * points[j].x
    return abs(area) / 2


while True:
    n = int(input())
    if n == 0:
        break
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    hull = andrew_monotone_chain(points)
    print(len(hull))
    for p in hull:
        print(p.x, p.y)

