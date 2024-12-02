N=int(input())
is_triangle=(N==3)
is_quadrilateral=(N==4)
is_pentagon=(N==5)
big_polygon=(N>5)
if is_triangle:
    print("Triangle")
elif is_quadrilateral:
    print("Quadrilateral")
elif  is_pentagon:
    print("Pentagon")
elif big_polygon:
    print("Big Polygon")
else:
    print("Not Polygon")