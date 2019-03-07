def d(n):
    tbt = 0
    for i in range(1, n, 1):
        if n % i == 0:
            tbt = tbt + i
    return tbt

sayac = 0
for a in range(1, 1000, 1):
    for b in range(1, 1000, 1):
        if a != b:
            if d(a) == b and d(b) == a:
                sayac = sayac + 1
                print("{} ve {} bağdaş sayıdır".format(a, b))

print(sayac)