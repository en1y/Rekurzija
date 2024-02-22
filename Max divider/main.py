def euclid(num1, num2):
    if num1 > num2: return euclid(num1 - num2, num2)
    elif num1 < num2: return euclid(num1, num2 - num1)
    else: return num1

print(euclid(22,33))