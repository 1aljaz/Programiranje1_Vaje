import math
import sys

def vekt_produkt(o, a, b):
    # Vektorski produkt OA x OB
    return (a[0] - o[0])*(b[1] - o[1]) - (a[1] - o[1])*(b[0] - o[0])

def convex_hull(points):
    # Andrew's monotone chain algorithm
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and vekt_produkt(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and vekt_produkt(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(points):
    # Shoelace formula za ploscino likov
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def polygon_perimeter(points):
    # obseh
    perimeter = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        dx = x2 - x1
        dy = y2 - y1
        perimeter += math.sqrt(dx*dx + dy*dy)
    return perimeter


input = sys.stdin.read().strip().split()
n, d, k = int(input[0]), float(input[1]), int(input[2])

points = [(float(input[2*i+3]), float(input[2*i+4])) for i in range(n)]

hull = convex_hull(points)
area = polygon_area(hull)
perimeter = polygon_perimeter(hull)

r = k * d
final_area = area + r * perimeter + math.pi * r * r
print(f"{final_area:.9f}")


