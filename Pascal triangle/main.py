def pascal_triangle(x, y):
    if y == 0 or x == y:
        return 1
    elif y > x:
        return 0
    else:
        return pascal_triangle(x-1, y-1)+pascal_triangle(x-1, y)
print(pascal_triangle(3,2))