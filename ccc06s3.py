def ccw(a, b, c):
    """Check if three points are listed in a counterclockwise order."""
    return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])
 
 
def segments_intersect(a, b, c, d):
    """Return True if line segments AB and CD intersect."""
    return (ccw(a, c, d) != ccw(b, c, d)) and (ccw(a, b, c) != ccw(a, b, d))
 
 
def point_on_segment(p, a, b):
    """Check if point p lies on segment ab."""
    if min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
        cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        return cross == 0
    return False
 
 
def line_intersects_polygon(p1, p2, polygon):
    """Check if line segment p1-p2 intersects or touches the polygon."""
    n = len(polygon)
    for i in range(n):
        a = polygon[i]
        b = polygon[(i + 1) % n]
        if segments_intersect(p1, p2, a, b) or point_on_segment(a, p1, p2) or point_on_segment(b, p1, p2):
            return True
    return False
 
 
def main():
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    buildings = []
    for _ in range(n):
        data = list(map(int, input().split()))
        k = data[0]
        coords = data[1:]
        polygon = [(coords[i], coords[i + 1]) for i in range(0, 2 * k, 2)]
        buildings.append(polygon)
 
    count = 0
    for building in buildings:
        if line_intersects_polygon((x1, y1), (x2, y2), building):
            count += 1
    print(count)
 
 
if __name__ == "__main__":
    main()