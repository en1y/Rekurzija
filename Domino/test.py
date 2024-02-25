import secrets
nl = [0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    num = secrets.choice(range(7))
    nl[num] += 1

[print(i) for i in nl]