word = input()
L1 = list(word)
L2 = []
length = len(L1)
#将L1中的字母去重，放入L2中
for i in L1:
    if i not in L2:
        L2.append(i)
count = 0
#找出L1中出现最多的字母，并计算出现的次数
#如果存在两个字母出现次数相同，取ASCII码较小的字母
for i in L2:
    if L1.count(i) > count:
        count = L1.count(i)
        letter = i
    elif L1.count(i) == count:
        if ord(i) < ord(letter):
            letter = i
#打印出现最多的字母和次数
print(letter)
print(count)