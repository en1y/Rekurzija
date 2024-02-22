def fact(num):
    if num > 1:
        return num * fact(num-1)
    else:
        return num

print(fact(4))