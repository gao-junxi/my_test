L1 = list()
L2 = list()
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        L1.append(i)
print("100以内的素数有：", L1)
length = len(L1)
for n in range(0, length-1):
    if L1[n] == L1[n+1] - 2:
        print(L1[n], L1[n+1], "是孪生数")
